import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

__version__ = '0.1.0'

# ver. 0.1.0    First working version

# URL of the website
# base_url = "https://hvidberg.net/Martin/Snaps_HDD/GEOSTAT/index.html"
base_url = "http://web.ais.dk/aisdata/"


time_2_wait_4_download = 6

# catch_dir = r"/home/martin/Downloads/"  # Linux
catch_dir = r"C:\Users\22016\Downloads"  # win

# Directory to save downloaded files
# download_dir = r"/home/martin/repos/EC_stuff/wscrap/downloaded_files/"  # Linux
# download_dir = r"C:\Users\22016\Martin\repos\EC_stuff\wscrap\downloaded_files"  # win
download_dir = r"C:\Users\22016\Downloads\wscrap"  # win


# Log file to track downloaded files
log_file = "download_log.txt"

def download_file(url, filename):

    ffn_a = os.path.join(catch_dir, filename.rsplit(os.sep, 1)[1])
    ffn_b = filename

    print(f"    init download_file({url}, {filename})")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    dic_expprefs = {"download.default_directory": catch_dir, "download.prompt_for_download": False}
    options.add_experimental_option("prefs", dic_expprefs);
    ddriver = webdriver.Chrome()
    ddriver.get(url)

    print(f"    Wait for the download to complete while monitoring: {ffn_a}")
    while True:
        if os.path.exists(ffn_a):
            break
        time.sleep(1)
    time.sleep(2)  # wait a few extra seconds to be safe ...
    print(f"    completed: {url}")
    print(f"    move file: {ffn_a} -> {ffn_b}")
    try:
        os.rename(ffn_a, ffn_b)
    except FileExistsError:
        print(f"WTF: FileExists: {ffn_b} !!! ErrNo.1737")
    except FileNotFoundError:
        print("WTF: FileNotFoundError !!! ErrNo.1736")

    ddriver.quit()

def update_log(filename):
    with open(log_file, "a") as log:
        log.write(f"{filename}\n")

def main():
    # Create download directory if not exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Read the existing log to avoid duplicates
    existing_files = set()
    if os.path.exists(log_file):
        with open(log_file, "r") as log:
            existing_files = set(log.read().splitlines())
    print(f"Existing log has: {len(existing_files)} files")

    # Start the browser and navigate to the website
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    print("starting Chrome driver ...")
    # driver = webdriver.Chrome(options=opts)  # Linux
    driver = webdriver.Chrome(options=opts)  # win
    print(f"Chrome driver started: {driver}")

    print(f"getting base url: {base_url}")
    driver.get(base_url)
    driver.refresh()
    print("Allow time for the page to load ...")
    time.sleep(5)  # Allow time for the page to load
    print(f" ... loaded: {driver.title}")

    file_links = driver.find_elements(By.PARTIAL_LINK_TEXT, ".zip")  # Update with the actual link text
    print(f"found: {len(file_links)} links")

    for link in file_links:
        str_furl = link.get_attribute("href")
        print(f" - lnk/href: {str_furl}")
        str_fn_in = str_furl.split("/")[-1]
        if str_fn_in not in existing_files:
            print(f"   ... going for: {str_furl}")
            str_path_ou = os.path.join(download_dir, str_fn_in)
            download_file(str_furl, str_path_ou)
            update_log(str_fn_in)
        else:
            print(f" .... skipping {str_furl}, all ready downloadet ...")

    driver.quit()

if __name__ == "__main__":
    main()

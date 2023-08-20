import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# URL of the website
base_url = "https://hvidberg.net/Martin/Snaps_HDD/GEOSTAT/index.html"

time_2_wait_4_download = 6

catch_dir = r"/home/martin/Downloads/"
# Directory to save downloaded files
download_dir = r"/home/martin/repos/EC_stuff/wscrap/downloaded_files/"

# Log file to track downloaded files
log_file = "download_log.txt"

def download_file(url, filename):

    print(f"    init download_file({url}, {filename})")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    dic_expprefs = {"download.default_directory": catch_dir, "download.prompt_for_download": False}
    options.add_experimental_option("prefs", dic_expprefs);

    # service = Service(r"/usr/bin/chromedriver")  # Update with the path to your chromedriver executable
    ddriver = webdriver.Chrome()
    print(f"    Download ddriver: {ddriver}")

    ddriver.get(url)
    # ddriver.refresh()
    time.sleep(time_2_wait_4_download)  # Allow time for the download to complete
    print(f"    got page")

    ffn_a = os.path.join(catch_dir, filename.rsplit(os.sep, 1)[1])
    ffn_b = filename
    print(f"    move file: {ffn_a} -> {ffn_b}")
    os.rename(ffn_a, ffn_b)

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
    driver = webdriver.Chrome(options=opts)
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

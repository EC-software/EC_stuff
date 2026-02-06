

import time
from datetime import datetime
import os
import platform

# === Configuration ===
target_time_str = "08:44:00"  # Format: HH:MM:SS (24-hour)
mp3_file_path = r"C:\Users\22016\Martin\repos\EC_stuff\alarm\sounds\Big-Ben-01.mp3"  # Change to your actual mp3 file path


def play_sound(file_path):
    system = platform.system()

    if system == "Windows":
        os.startfile(file_path)
    elif system == "Darwin":  # macOS
        os.system(f"afplay '{file_path}'")
    elif system == "Linux":
        os.system(f"xdg-open '{file_path}'")
    else:
        print("Unsupported OS for playing sound.")


def wait_until(target_time_str):
    print(f"Waiting until {target_time_str}...")

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == target_time_str:
            print("Time reached! Playing sound...")
            play_sound(mp3_file_path)
            break
        time.sleep(0.5)


# Run it
wait_until(target_time_str)

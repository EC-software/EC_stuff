import os

def create_file_list(directory):
    try:
        file_list = os.listdir(directory)
        with open(os.path.join(directory, 'file_list.txt'), 'w') as file:
            for filename in file_list:
                if filename.lower().endswith('.jpg'):
                    file_path = os.path.join(directory, filename)
                    file_size = os.path.getsize(file_path)
                    file.write(f"{filename}, {file_size}\n")
        print(f"File list created in {directory}")
    except Exception as e:
        print(f"Error creating file list in {directory}: {e}")

def main(root_directory):
    for root, _, _ in os.walk(root_directory):
        create_file_list(root)

if __name__ == "__main__":
    starting_directory = r"/home/martin/Pictures/DCIM/100ANDRO/20230815_Skjoldunge_2/"
    main(starting_directory)

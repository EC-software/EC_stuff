
# mainly ChactGPT generated ...

data = r"data/samp1.txt"

def read_special_format_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if not lines[i].strip().isdigit() and not any(char.isdigit() for char in lines[i]):
            first_line = lines[i].strip()
            i += 1

            if not lines[i].strip().isdigit() and not any(char.isdigit() for char in lines[i]):
                second_line = lines[i].strip()
                i += 1

                mixed_lines = []
                while i < len(lines) and any(char.isdigit() for char in lines[i]):
                    mixed_lines.append(lines[i].strip())
                    i += 1

                # Print or process the group of lines
                print("Group:")
                print(first_line)
                print(second_line)
                for mixed_line in mixed_lines:
                    print(mixed_line)
                print()
            else:
                print(f"Unexpected format: Line {i} should be text without numbers.")
                break
        else:
            print(f"Unexpected format: Line {i} should be text without numbers.")
            break


# Example usage
file_path = data
read_special_format_file(file_path)

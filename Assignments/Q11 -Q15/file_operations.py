# file_operations.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except IOError as e:
        return f"Error reading file: {e}"

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Data written successfully."
    except IOError as e:
        return f"Error writing to file: {e}"

def append_to_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return "Data appended successfully."
    except IOError as e:
        return f"Error appending to file: {e}"

if __name__ == "__main__":
    # Test the functions here
    file_path = 'example.txt'
    print(write_file(file_path, 'This is a new file.\n'))
    print(append_to_file(file_path, 'Appending some more text.\n'))
    print("File Content:")
    print(read_file(file_path))

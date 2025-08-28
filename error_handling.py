def read_file_simple():
    while True:
        try:
            filename = input("Enter filename: ").strip()
            with open(filename, 'r') as f:
                return f.read(), filename
        except FileNotFoundError:
            print("File doesn't exist. Try again.")
        except:
            print("Error reading file. Try again.")

# Usage
content, filename = read_file_simple()
print(f"Read {len(content)} characters from {filename}")

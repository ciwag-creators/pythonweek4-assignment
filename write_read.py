def reading_file(input_file, output_file):
    """
    Reads a file, modifies its content, and writes to a new file
    """
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"File successfully modified and saved as '{output_file}'")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
modify_file('input.txt', 'output.txt')

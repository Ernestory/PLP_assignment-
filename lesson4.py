def process_file():
    filename = input("Enter the name of the file to read:input.txt ")

    try:
        # Try to open and read the original file
        with open(filename, "r") as original_file:
            content = original_file.read()
            print("✅ File read successfully!")

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create new filename and write modified content
        new_filename = f"modified_{filename}"
        with open(new_filename, "w") as modified_file:
            modified_file.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write the file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
process_file()

file_path = "Validator\schemas\edges_schema.json"

# Step 1: Open the file
with open(file_path, "r") as file:
    # Step 2: Read the contents
    contents = file.read()

    # Step 3: Print the contents
    print(contents)

# The file will be automatically closed once the 'with' block is exited

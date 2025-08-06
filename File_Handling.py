# Writing to a file
try:
    with open("example.txt", "w") as file:
        file.write("Hello!\n")
    print("Data written to file successfully.")
except IOError:
    print("Error: Failed to write to the file.")

# Reading from the file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nFile Content:\n" + content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Could not read the file.")
# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# Define the main function
def main():
    # Ask the user for the name of a file
    file = input("File name: ")
    # Check the file's media type and print it
    print(check_filetype(file))

# Define a function that checks a file's media type based on its extension
def check_filetype(filetype):
    # Split the filename into name and extension
    file_ext = filetype.split(".")
    # Use a match-case structure to check the file extension
    match file_ext[1]:
        # If the extension is gif, jpg, or png, it's an image file
        case "gif" | "jpg" | "png":
            return "image/" + file_ext[1]
        # If the extension is jpeg, it's an image file
        case "jpeg":
            return "image/jpeg"
        # If the extension is pdf, txt, or zip, it's an application file
        case "pdf" | "txt" | "zip":
            return "application/" + file_ext[1]
        # If the extension is anything else, it's an unknown file type
        case _:
            return "Unknow file type."

# Call the main function
main()
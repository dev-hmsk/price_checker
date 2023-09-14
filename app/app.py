import os
import platform
import pdfplumber

 # Python Script Directory
print("Current working directory:", os.getcwd())
app_directory = os.path.dirname(os.path.abspath(__file__))
print(app_directory)

# Check OS
system = platform.system()

if system == "Linux":  # Execute Linux Code Block

    # Get the user's home directory
    user_home = os.path.expanduser("~")
    # Get relevant directory locations
    app_directory = os.path.join(user_home, app_directory)
    parent_directory = os.path.dirname(app_directory)
    document_directory = os.path.join(parent_directory, "documents")
    print(document_directory)

def find_file(directory, file_list):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(f"Found file: {item_path}")
            file_list.append(item_path)
        elif os.path.isdir(item_path):
            print(f"Entering directory: {item_path}")
            find_file(item_path, file_list)
    
file_list = []

find_file(document_directory, file_list)

for item in file_list:
    print(item)
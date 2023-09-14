import os
import platform
import pytesseract
from pdf2image import convert_from_path
# import cv2

# Python Script Directory
app_directory = os.path.dirname(os.path.abspath(__file__))


# Check OS
system = platform.system()

if system == "Linux":  # Execute Linux Code Block

    # Get the user's home directory
    user_home = os.path.expanduser("~")
    # Get relevant directory locations
    app_directory = os.path.join(user_home, app_directory)
    parent_directory = os.path.dirname(app_directory)
    document_directory = os.path.join(parent_directory, "documents")
    image_directory = os.path.join(parent_directory,"images")
    ocr_directory = os.path.join(parent_directory, "ocr")
    # print(document_directory)

# Recursively find all files within a given directory and append them to a list
def find_file(directory, file_list):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item != ".gitkeep" : # We can later add specificy to only add certain file types like .pdf. Currently set to ignore .gitkeep
            # print(f"Found file: {item_path}") 
            file_list.append(item_path)
        elif os.path.isdir(item_path):
            # print(f"Entering directory: {item_path}")
            find_file(item_path, file_list)


file_list = []
find_file(document_directory, file_list)

# Convery the .pdf to .bmp files
for item in file_list:
    # Set file save names
    item_base_name = os.path.basename(item)
    item_base_name_w_o_ext = item_base_name.rstrip(".pdf")
    images = convert_from_path(item)
    output_folder = image_directory

    for i, image in enumerate(images):
        bmp_file = f'{output_folder}/{item_base_name_w_o_ext}_page_{i + 1}.bmp'
        image.save(bmp_file, 'BMP')

bmp_files = []
find_file(image_directory,bmp_files)

# Read the .bmp files using Tesseract OCR and save them as text
for bmp_file in bmp_files:
    # print(bmp_file)
    text = pytesseract.image_to_string(bmp_file)
    item_base_name = os.path.basename(bmp_file)
    item_base_name_w_o_ext = item_base_name.rstrip(".bmp")
    text_file_location = os.path.join(ocr_directory, item_base_name_w_o_ext)
    # print(text_file_location)
    with open(text_file_location, 'w', encoding='utf-8') as file:
        file.write(text)
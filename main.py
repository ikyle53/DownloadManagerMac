import os
from pathlib import Path

downloads = Path("/Users/Kylu/Downloads")

# List of file types for images
images = ['.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.jfif', '.svg', '.tif', '.tiff', '.HEIC']

# List of file types for documents and other things
data = ['.xls', '.xlsx', '.csv', '.pages', '.doc', '.docx']

pdfs = ['.pdf']

# Create an images folder if it doesn't exist
if os.path.isdir(f'{downloads}/Images') == False:
    os.mkdir(f'{downloads}/Images')

# Create a data folder if it doesn't exist
if os.path.isdir(f'{downloads}/Data') == False:
    os.mkdir(f'{downloads}/Data')

# Create a pdf folder if it doesn't exist
if os.path.isdir(f'{downloads}/PDFs') == False:
    os.mkdir(f'{downloads}/PDFs')

# Create an other folder if it doens't exist
if os.path.isdir(f'{downloads}/Other') == False:
    os.mkdir(f'{downloads}/Other')

# Iterate through the files in the downloads folder
for file in downloads.iterdir():
    # Gotta check if it's a system file
    if file.is_file() and file.stem != ".DS_Store" and file.stem != ".localized":
        file_name = file.stem
        extension = file.suffix

        # Now to move files that match the lists above
        if (extension in images):
            file.replace(f'{file.parent}/Images/{file_name}{extension}')
        elif (extension in data):
            file.replace(f'{downloads}/Data/{file_name}{extension}')
        elif (extension in pdfs):
            file.replace(f'{downloads}/PDFs/{file_name}{extension}')
        else:
            file.replace(f'{downloads}/Other/{file_name}{extension}')

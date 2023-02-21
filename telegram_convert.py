# This program takes most images and scales down the largest dimension (x or y) to 512.
# The intention is to convert an image to being Telegram sticker compatible.
# Requires Python 3 and the Pillow module.

# To run:
#  1. Install Python 3: https://www.python.org/downloads/
#  2. Install the Pillow module. After installing Python, open a cmd prompt and run: pip install pillow
#  3. Navigate to the directory with your images you want to convert by doing one of the following:
#    a. In a cmd window, run: cd <path to images>
#    b. Or, shift-right click in the folder with your images, and click "open PowerShell window here"
#  4. Run the script: py telegram_convert.py
#  5. The telegram compatible stickers will be in the 'converted_telegram' folder.

from __future__ import with_statement
import os
from PIL import Image

CONVERTED_FOLDER_NAME = "converted_telegram"

image_path = os.getcwd()
print(image_path)
if not os.path.exists(CONVERTED_FOLDER_NAME):
    os.makedirs(CONVERTED_FOLDER_NAME)

counter = 0
for file in os.listdir(image_path):
    f = file
    filename, extension = os.path.splitext(file) # grabs the extension
    try: 
        with Image.open(f, 'r') as im:
            sizeX = im.size[0]
            sizeY = im.size[1]
            if sizeX >= sizeY:
                if sizeX >= 512:
                    diff = sizeX - 512
                    resized = im.resize((512,sizeY - diff))
                else:
                    diff = 512 - sizeX
                    resized = im.resize((512,sizeY + diff))
            else:
                if sizeY >= 512:
                    diff = sizeY - 512
                    resized = im.resize((sizeX - diff, 512))
                else:
                    diff = 512 - sizeY
                    resized = im.resize((sizeX + diff, 512))
            resized.save(f"{CONVERTED_FOLDER_NAME}/resized_{counter}{extension}")
            counter += 1
    except Exception as error: # this is how we can do any image supported by pillow
        #print(error) #debug
        continue

print(f"{counter} stickers placed in: {os.getcwd()}")

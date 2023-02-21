# This program takes most images and scales down the largest dimension (x or y) to LARGEST_DIMENSION.
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

LARGEST_DIMENSION = 512 # Change to alter the generated image's minimum dimension size

image_path = os.getcwd()

i = 0
temp = CONVERTED_FOLDER_NAME
if os.path.exists(CONVERTED_FOLDER_NAME):
    while os.path.exists(temp):
        temp = CONVERTED_FOLDER_NAME + "_" + str(i)
        i += 1
    CONVERTED_FOLDER_NAME = temp
    
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
                ratio = sizeY / sizeX
                if scaled_val > LARGEST_DIMENSION: # if in some freak incident where it could round
                    scaled_val = LARGEST_DIMENSION # above the largest dimension that is set, prevent that.
                resized = im.resize((LARGEST_DIMENSION, round(ratio * LARGEST_DIMENSION)))
            else:
                ratio = sizeX / sizeY
                scaled_val = round(ratio * LARGEST_DIMENSION)
                
                if scaled_val > LARGEST_DIMENSION: # if in some freak incident where it could round
                    scaled_val = LARGEST_DIMENSION # above the largest dimension that is set, prevent that.
                resized = im.resize((scaled_val, LARGEST_DIMENSION))
                
            resized.save(f"{CONVERTED_FOLDER_NAME}/resized_{counter}{extension}")
            counter += 1
    except Exception as error: # this is a lazy way to handle any image supported by pillow
                               # it continues searching if it doesn't find a compatible image file
        #print(error) #debug
        continue

print(f"{counter} stickers placed in: {os.getcwd()}/{CONVERTED_FOLDER_NAME}")

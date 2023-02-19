# telegram-sticker-converter
Converts a bunch of images to be compatible with Telegram.

# Description 
This program takes most images and scales down the largest dimension (x or y) to 512.
The intention is to convert an image to being Telegram sticker compatible.
Requires Python 3 and the Pillow module.

# To Run
 1. Install Python 3: https://www.python.org/downloads/
 2. Install the Pillow module. After installing Python, open a cmd prompt and run: pip install pillow
 3. Navigate to the directory with your images you want to convert by doing one of the following:
    - In a cmd window, run: cd [path to images]
    - Or, shift-right click in the folder with your images, and click "open PowerShell window here"
 4. Run the script: py telegram_convert.py
 5. The telegram compatible stickers will be in the 'converted_telegram' folder.

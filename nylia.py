#Install https://github.com/UB-Mannheim/tesseract/wiki
# Libraries: pip install pytesseract, pip install Pillow

from PIL import Image
from pytesseract import *
try:
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    file_n = input('File name: ') # Enter the name of the txt file to create (any name), ending with .txt


    img = Image.open(input('Image name: ')) 
    """                                        Enter the name of the image that is in your 
                                               folder in the location of your program,
                                               ending with .png or ending with your image.
    """



    outp = pytesseract.image_to_string(img)
    f = open(file_n,'w')
    f.write(outp)
    f.close()
    print('Successful program!')
except OSError as e:
    print('File name error or name imagen :(' )


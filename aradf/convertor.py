import cv2 
import pytesseract
import numpy as np
from typing import Tuple
import fitz
from PIL import Image


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
def extract_text(image):
    gray = get_grayscale(image)
    gray = thresholding(gray)
    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(gray, config=custom_config,lang="ara")
    return text

def convert_pdf2img(input_file: str, pages: Tuple = None):
    """Converts pdf to image and generates a file by page"""
    # Open the document
    pdfIn = fitz.open(input_file)
    output_files = []
    # Iterate throughout the pages
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        # Select a page
        page = pdfIn[pg]
        rotate = int(0)
        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        output_files.append(img)
    pdfIn.close()
  
    return output_files, input_file


def pdf_to_txt(path: str):
    path =r''+path
    path = path.replace("\\","/")
    images, book = convert_pdf2img(path)
    print(path)
    page_num = 1
    total_text = ""  
    for im in images:
        page_text = "################## PAGE: " + str(page_num) + " ####################\n"
        print("Page: " + str(page_num))
        open_cv_image = np.array(im) 
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        text = page_text +"\n" + extract_text(open_cv_image)+"\n"
        total_text += text
        page_num+=1
    print(book)
    book = book.replace("pdf", "txt")
    print("Converting : " + book)
    with open(book, "w",encoding = 'utf-8') as text_file:
         text_file.write(total_text)
    print("DONE!")
    return total_text


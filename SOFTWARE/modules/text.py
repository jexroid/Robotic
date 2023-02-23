import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kigir\Documents\TESSERACT\tesseract.exe"
def rext_reader(frame):

    resault = (pytesseract.image_to_string(frame))
    return resault



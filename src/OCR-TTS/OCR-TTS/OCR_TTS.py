from PIL import Image
import pytesseract
from gtts import gTTS
import cv2
from typing import Text
import sys

a = int(input("English = 1, Korean = 2 : ")

image = cv2.imread('n1.PNG')

if image is None:
    print("Image file Error")
    sys.exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

if a==1:
    lan="eng"
    lan2="en"
elif a==2:
    lan="kor"
    lan2="ko"
else:
    print("Language Error")
    sys.exit()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr_text = pytesseract.image_to_string(image, lang=lan)
print(ocr_text.replace(" ",""))

with open("news.txt","w",encoding="utf8") as f:
    f.write("\n\n\n")
    f.write(ocr_text.replace(" ",""))

#txt파일 mp3파일로 변환
conversion = 'news.txt'

with open(conversion, mode = 'r', encoding='UTF-8') as text:
    script = text.read()

speech = gTTS(text = script, lang=lan2)
speech.save('read_news.mp3')

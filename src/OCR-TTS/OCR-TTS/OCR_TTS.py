from PIL import Image
import pytesseract
from gtts import gTTS
import cv2

image = cv2.imread('n1.PNG')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr_text = pytesseract.image_to_string(image, lang="kor")
print(ocr_text.replace(" ",""))

with open("news.txt","w",encoding="utf8") as f:
    f.write("\n\n\n")
    f.write(ocr_text.replace(" ",""))

#txt파일 mp3파일로 변환
conversion = 'news.txt'

with open(conversion, mode = 'r', encoding='UTF-8') as text:
    script = text.read()

speech = gTTS(text = script, lang='ko')
speech.save('read_news.mp3')

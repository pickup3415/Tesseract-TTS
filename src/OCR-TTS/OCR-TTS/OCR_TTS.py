from PIL import Image
import pytesseract
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr_text = pytesseract.image_to_string(Image.open("n1.PNG"), lang="kor")
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
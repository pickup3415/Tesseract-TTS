from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("C:\\Users\\USER\\source\\repos\\OCR-TTS\\n1.PNG"), lang="kor")
print(text)
print(text.replace(" ",""))

with open("news.txt","w",encoding="utf8") as f:
    f.write(text)
    f.write("\n\n\n")
    f.write(text.replace(" ",""))

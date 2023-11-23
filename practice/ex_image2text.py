import pytesseract
from PIL import Image

image = Image.open('/Users/hanjeonghyeon/Desktop/homework_py/capture_app/captured_image.png')
#pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract' #TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information. 에러 메시지 나올 경우
text = pytesseract.image_to_string(image, lang='kor')
print(text)

import cv2
from PIL import Image

import pytesseract
import numpy as np



def bound2Text(name):

    image = cv2.imread(name)

    # 이미지를 그레이스케일로 변환하는 함수 호출
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold_image = cv2.threshold(gray_image, 125, 255, cv2.THRESH_BINARY)

    invert = 255 - threshold_image

    # 글자의 경계를 팽창시켜 두껍게 만듦
    kernel = np.ones((3, 3), np.uint8)
    invert = cv2.dilate(invert, kernel=kernel, iterations=8) # , anchor=(0,1)

    contours, _ = cv2.findContours(invert, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    dst2 = cv2.cvtColor(invert, cv2.COLOR_GRAY2BGR)

    text_save = []

    # 각 윤곽선에 대해 사각형 그리기
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        print(x, y, w, h)
        cv2.rectangle(dst2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped_area = gray_image[y:y+h, x:x+w]

        text = pytesseract.image_to_string(cropped_area, lang='kor')
        print(text)
        text_save.append(text)

    print(text_save)
    return text_save


txt = []

for i in range(0, 50):
    ToSave = bound2Text('data/' + str(i) + '.png')
    txt.append(ToSave)

with open("save.txt", 'w', encoding='utf-8') as save_txt:
    for index, t in enumerate(txt):
        save_txt.write(r"{}===============================================\n".format(index))
        save_txt.write('&'.join(t))
        save_txt.write('\n')







"""
with open(파일명, 'w', encoding='utf-8') as 파일:
    파일.write(내용)

cv2.imshow("Color", image)
cv2.imshow("gray", gray_image)
cv2.imshow("thhlod", threshold_image)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyWindow()

"""

import cv2
from PIL import Image
import numpy as np
image = cv2.imread("data/4.png")


# 이미지를 그레이스케일로 변환하는 함수 호출
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image_d = gray_image.copy()
# 스레시홀드 적용 (예시 기준 값은 127)
_, threshold_image = cv2.threshold(gray_image, 125, 255, cv2.THRESH_BINARY)

invert = 255 - threshold_image

# 팽창 연산을 위한 커널 생성
kernel = np.ones((3, 3), np.uint8)
print(kernel)

# 글자의 경계를 팽창시켜 두껍게 만듦
invert = cv2.dilate(invert, kernel=kernel, iterations=8) # , anchor=(0,1)

contours, _ = cv2.findContours(invert, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

dst2 = cv2.cvtColor(invert, cv2.COLOR_GRAY2BGR)
# 각 윤곽선에 대해 사각형 그리기
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(x, y, w, h)
    cv2.rectangle(dst2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Or", image)
cv2.imshow("thhlod", threshold_image)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyWindow()
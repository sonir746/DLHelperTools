import cv2
from dlhelpertools import padding
color=(0,0,255)
img=cv2.imread(R"test_\img\img.jpg")
padding.img_resize_and_paddig(img, show=True)
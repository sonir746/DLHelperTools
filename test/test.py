import cv2
from dlhelpertools import padding
color=(0,0,255)
img=cv2.imread(R"C:\Users\WORK\Documents\GIT\dlhelpertools\test\img\img.jpg")
padding.img_resize_and_paddig(img, show=True, save=True, color=color,size=(300,400) ,path=rf"C:\Users\WORK\Documents\GIT\dlhelpertools\test\img")
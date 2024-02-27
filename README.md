# dlhelpertools

This dlhelpertools is designed to help ai model building

## Packages Used

| **Package** | **Version** |
| ----------- | ----------- |
| Python      | 3.8         |
| OpenCV      | 4.8.1       |
| numpy       | 1.26.4      |

## Testing

### Sample input image

<center><img src="test\img\img.jpg" alt="loading..." /></center>

## Source Code

```Python
import cv2
from dlhelpertools import padding

img=cv2.imread(R"img.jpg")

padding.img_resize_and_paddig(img, show=True, save=True)
```

### Output image

<center><img src="test\img\padded.jpg" alt="loading..."/></center>

<br>

Default image size is (224x224)<br>
you can give custom size using

```Python
path = RF"path_for_save"

padding.img_resize_and_paddig(img, show=True, save=True, size=(300, 400) ,path=path)
```

## Output Image

<center><img src="test\img\padded1709017389.819483.jpg" alt="loading..."/></center>
<br>
By Default we use white padding (255, 255, 255)<br>
You can also use diff. color padding<br>
NOTE: color in **BGR** formate<br>
<br>

```Python
Red=(0,0,255) # color in BGR formate

padding.img_resize_and_paddig(img, show=True, save=True, color=Red,size=(300,400))
```

<br>

## Output Image

<center><img src="test\img\padded1709017926.6538558.jpg" alt="loading..."/></center>


## Auther

👨🏻‍💼RAHUL SONI

[![linkedin](https://img.shields.io/twitter/url?url=https%3A%2F%2Fwww.linkedin.com&style=social&logo=Linkedin&logoColor=White&label=Linkedin&labelColor=blue&color=blue&cacheSeconds=3600
)](https://www.linkedin.com/in/rahul-soni-004861227)
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2F&style=social&logo=GitHub&logoColor=Black&label=GitHub&labelColor=abcdef&color=fedcba&cacheSeconds=3600
)](https://github.com/rahulsoni746)



## Feedback

If you have any feedback, please reach out to us at rahulsoni@gmail.com

Or

Report any issue here
<br>
👇👇👇
<br>
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com&style=social&logo=GitHub&label=issue&labelColor=grey&color=grey
)](https://github.com/rahulsoni746/dlhelper_tools/issues)
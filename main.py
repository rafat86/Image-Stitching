import numpy
import cv2
import numpy as np
from PIL import Image

img_2 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/Fr01.jpg")
img_1 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/Fr02.jpg")

img_1.show()
img_2.show()

size_1 = img_1.size
size_2 = img_2.size

upper_list_img_1 = []
right_list_img_1 = []
down_list_img_1 = []
left_list_img_1 = []

upper_list_img_2 = []
right_list_img_2 = []
down_list_img_2 = []
left_list_img_2 = []

for i in range(size_1[0]):
    in_pixel = img_1.getpixel((i, 0))
    upper_list_img_1.append(in_pixel)

i = size_1[0]
for j in range(size_1[1]):
    in_pixel = img_1.getpixel((i-1, j))
    right_list_img_1.append(in_pixel)

j = size_1[1]
for i in range(size_1[0]):
    in_pixel = img_1.getpixel((i, j-1))
    down_list_img_1.append(in_pixel)

for j in range(size_1[1]):
    in_pixel = img_1.getpixel((0, j))
    left_list_img_1.append(in_pixel)

for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, 0))
    upper_list_img_2.append(in_pixel)

i = size_2[0]
for j in range(size_2[1]):
    in_pixel = img_2.getpixel((i-1, j))
    right_list_img_2.append(in_pixel)

j = size_2[1]
for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, j-1))
    down_list_img_2.append(in_pixel)

for j in range(size_2[1]):
    in_pixel = img_2.getpixel((0, j))
    left_list_img_2.append(in_pixel)

array_upper_list_img_1 = np.array(upper_list_img_1)
array_right_list_img_1 = np.array(right_list_img_1)
array_down_list_img_1 = np.array(down_list_img_1)
array_left_list_img_1 = np.array(left_list_img_1)

array_upper_list_img_2 = np.array(upper_list_img_2)
array_right_list_img_2 = np.array(right_list_img_2)
array_down_list_img_2 = np.array(down_list_img_2)
array_left_list_img_2 = np.array(left_list_img_2)

def rms(array_1,array_2):
    return np.sqrt(((array_1 - array_2) ** 2).mean())

if size_1[0] == size_2[0] == size_1[1] == size_2[1] :
        rms_min = min(rms(array_upper_list_img_1, array_down_list_img_2),
                      rms(array_down_list_img_1, array_upper_list_img_2),
                      rms(array_right_list_img_1, array_left_list_img_2),
                      rms(array_left_list_img_1, array_right_list_img_2))
elif size_1[0] == size_2[0]:
        rms_min = min(rms(array_upper_list_img_1, array_down_list_img_2),
                  rms(array_down_list_img_1, array_upper_list_img_2))
elif size_1[1] == size_2[1]:
        rms_min = min(rms(array_right_list_img_1, array_left_list_img_2),
                  rms(array_left_list_img_1, array_right_list_img_2))


if rms_min == rms(array_upper_list_img_1, array_down_list_img_2):
    new_image = Image.new('RGB', (size_1[0],(2 * size_1[1])))
    new_image.paste(img_2, (0, 0))
    new_image.paste(img_1, (0, size_2[1]))
    new_image.show()
elif rms_min ==  rms(array_down_list_img_1, array_upper_list_img_2) :
    new_image = Image.new('RGB', (size_1[0],(2 * size_1[1])))
    new_image.paste(img_1, (0, 0))
    new_image.paste(img_2, (0, size_1[1]))
    new_image.show()
elif rms_min == rms(array_right_list_img_1, array_left_list_img_2) :
    new_image = Image.new('RGB', (2 * size_1[0], size_1[1]))
    new_image.paste(img_1, (0, 0))
    new_image.paste(img_2, (size_1[0],0 ))
    new_image.show()
elif rms_min == rms(array_left_list_img_1, array_right_list_img_2) :
    new_image = Image.new('RGB', (2 * size_1[0], size_1[1]))
    new_image.paste(img_2, (0, 0))
    new_image.paste(img_1, (size_1[0],0 ))
    new_image.show()

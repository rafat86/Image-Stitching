import numpy as np
from PIL import Image

print(" 1-Eiffel Tower", "\n", "2-Jerusalem City ", "\n", "3-River ")

reader_choice = int(input("chose a picture to stitch:"))

while reader_choice not in range(4):
    reader_choice = int(input("chose a picture to stitch:"))

if reader_choice == 1:
    img_1 = Image.open("test images/eiffel.jpg")
    img_2 = Image.open("test images/eiffel02.jpg")
if reader_choice == 2:
    img_1 = Image.open("test images/Jerusalem01.jpg")
    img_2 = Image.open("test images/Jerusalem02.jpg")
if reader_choice == 3:
    img_1 = Image.open("test images/Fr01.jpg")
    img_2 = Image.open("test images/Fr02.jpg")

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

for j in range(size_1[1]):
    in_pixel = img_1.getpixel((size_1[0] - 1, j))
    right_list_img_1.append(in_pixel)

for i in range(size_1[0]):
    in_pixel = img_1.getpixel((i, size_1[1] - 1))
    down_list_img_1.append(in_pixel)

for j in range(size_1[1]):
    in_pixel = img_1.getpixel((0, j))
    left_list_img_1.append(in_pixel)

for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, 0))
    upper_list_img_2.append(in_pixel)

for j in range(size_2[1]):
    in_pixel = img_2.getpixel((size_2[0] - 1, j))
    right_list_img_2.append(in_pixel)

for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, size_2[1] - 1))
    down_list_img_2.append(in_pixel)

for j in range(size_2[1]):
    in_pixel = img_2.getpixel((0, j))
    left_list_img_2.append(in_pixel)

    def edges(pixel_list):
        return np.array(pixel_list)

    def rms(array_1, array_2):
        return np.sqrt(((array_1 - array_2) ** 2).mean())

if size_1[0] == size_2[0] == size_1[1] == size_2[1]:
    rms_min = min(rms(edges(upper_list_img_1), edges(down_list_img_2)),
                  rms(edges(down_list_img_1), edges(upper_list_img_2)),
                  rms(edges(right_list_img_1), edges(left_list_img_2)),
                  rms(edges(left_list_img_1), edges(right_list_img_2)))
elif size_1[0] == size_2[0]:
    rms_min = min(rms(edges(upper_list_img_1), edges(down_list_img_2)),
                  rms(edges(down_list_img_1), edges(upper_list_img_2)))
elif size_1[1] == size_2[1]:
    rms_min = min(rms(edges(right_list_img_1), edges(left_list_img_2)),
                  rms(edges(left_list_img_1), edges(right_list_img_2)))

if rms_min == rms(edges(upper_list_img_1), edges(down_list_img_2)):
    new_image = Image.new('RGB', (size_1[0], (2 * size_1[1])))
    new_image.paste(img_2, (0, 0))
    new_image.paste(img_1, (0, size_2[1]))
    new_image.show()
elif rms_min == rms(edges(down_list_img_1), edges(upper_list_img_2)):
    new_image = Image.new('RGB', (size_1[0], (2 * size_1[1])))
    new_image.paste(img_1, (0, 0))
    new_image.paste(img_2, (0, size_1[1]))
    new_image.show()
elif rms_min == rms(edges(right_list_img_1), edges(left_list_img_2)):
    new_image = Image.new('RGB', (2 * size_1[0], size_1[1]))
    new_image.paste(img_1, (0, 0))
    new_image.paste(img_2, (size_1[0], 0))
    new_image.show()
elif rms_min == rms(edges(left_list_img_1), edges(right_list_img_2)):
    new_image = Image.new('RGB', (2 * size_1[0], size_1[1]))
    new_image.paste(img_2, (0, 0))
    new_image.paste(img_1, (size_1[0], 0))
    new_image.show()

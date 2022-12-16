from PIL import Image

img_1 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/eifel.jpg")
img_2 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/eifel02.jpg")

#print(img_1.format)
print(img_1.size)
#print(img_1.mode)
#img_1.show()
#img_2.show()

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
print(upper_list_img_1)

i = size_1[0]
for j in range(size_1[1]):
    in_pixel = img_1.getpixel((i-1, j))
    right_list_img_1.append(in_pixel)
print(right_list_img_1)

j = size_1[1]
for i in range(size_1[0]):
    in_pixel = img_1.getpixel((i, j-1))
    down_list_img_1.append(in_pixel)
print(down_list_img_1)

for j in range(size_1[1]):
    in_pixel = img_1.getpixel((0, j))
    left_list_img_1.append(in_pixel)
print(left_list_img_1)

for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, 0))
    upper_list_img_2.append(in_pixel)
print(upper_list_img_2)

i = size_2[0]
for j in range(size_2[1]):
    in_pixel = img_2.getpixel((i-1, j))
    right_list_img_2.append(in_pixel)
print(right_list_img_2)

j = size_2[1]
for i in range(size_2[0]):
    in_pixel = img_2.getpixel((i, j-1))
    down_list_img_2.append(in_pixel)
print(down_list_img_2)

for j in range(size_2[1]):
    in_pixel = img_2.getpixel((0, j))
    left_list_img_2.append(in_pixel)
print(left_list_img_2)

#print(list_img_2)
list_11 = img_1.getpixel((0,0))
list_22 = img_1.getpixel((100, 0))





array_upper_list_img_1 = np.array(upper_list_img_1)
array_right_list_img_1 = np.array(right_list_img_1)
array_down_list_img_1 = np.array(down_list_img_1)
array_left_list_img_1 = np.array(left_list_img_1)

array_upper_list_img_2 = np.array(upper_list_img_2)
array_right_list_img_2 = np.array(right_list_img_2)
array_down_list_img_2 = np.array(down_list_img_2)
array_left_list_img_2 = np.array(left_list_img_2)
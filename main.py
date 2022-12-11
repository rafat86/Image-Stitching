from PIL import Image

full_img_1 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/eifel.jpg")
full_img_2 = Image.open("C:/Users/RAFAT/Documents/GitHub/HW3-Image-Stitching/test images/eifel02.jpg")

img_1 = full_img_1.convert("L")
img_2 = full_img_2.convert("L")

print(img_1.format)
print(img_1.size)
print(img_1.mode)

print(img_2.format)
print(img_2.size)
print(img_2.mode)

#img_1.show()
#img_2.show()

size_1 = img_1.size
size_2 = img_2.size

list_img_1 = []

for i in range(1):
    for j in range(size_1[0]):
        in_pixel = img_1.getpixel((i, j))
        list_img_1.append(in_pixel)
print(list_img_1)

list_img_2 = []

for i in range(size_2[0]):
    for j in range(1):
        in_pixel = img_2.getpixel((i, j))
        list_img_2.append(in_pixel)

print(list_img_2)

list_11 =  img_1.getpixel((467, 468))
list_22 =  img_2.getpixel((0, 0))

print(list_11)
print(list_22)
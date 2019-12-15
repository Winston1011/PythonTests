from PIL import Image

img = Image.open("432.jpg")
area = (100, 100, 350, 395)
cropped_img = img.crop(area)

#img.show()
cropped_img.show()
from PIL import Image

img = Image.open("432.jpg")
print(img.size)
print(img.format)

img.show()
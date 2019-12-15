from PIL import Image

leave = Image.open("leave.jpg")
bucky = Image.open("432.jpg")

print(bucky.size)
print(leave.size)
area = (100, 100, 677, 677)
leave.paste(bucky, area)

leave.show()
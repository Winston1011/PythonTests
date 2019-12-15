from PIL import Image

leave = Image.open("leave.jpg")
#print(leave.mode)
r, g, b = leave.split()

new_img = Image.merge("RGB", (r, g, b))
new_img1 = Image.merge("RGB", (b, r, g))
#r.show()
#g.show()
#b.show()
#new_img.show()
new_img1.show()
from PIL import Image

bucky = Image.open("432.jpg")
flip_bucky = bucky.transpose(Image.FLIP_LEFT_RIGHT)
spin_bucky = bucky.transpose(Image.ROTATE_90)

flip_bucky.show()
#spin_bucky.show()

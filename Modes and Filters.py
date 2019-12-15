from PIL import Image
from PIL import ImageFilter

bucky = Image.open("432.jpg")
blur = bucky.filter(ImageFilter.BLUR)
detail = bucky.filter(ImageFilter.DETAIL)
edges = bucky.filter(ImageFilter.FIND_EDGES)

#blur.show()
#detail.show()
edges.show()
from PIL import Image
from PIL import ImageFilter
im = Image.open("C:/Users/WOOKING/Desktop/1.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("2.jpg")
from PIL import Image
from PIL import ImageEnhance
im = Image.open("C:/Users/WOOKING/Desktop/1.jpg")
om = ImageEnhance.Contrast(im)
om.enhance(20).save("3.jpg")
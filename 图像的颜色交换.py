from PIL import Image
im = Image.open("C:/Users/WOOKING/Desktop/1.jpg")
r, g, b = im.split()
om = Image.merge("RGB",(r,g,b))
om.save("a.jpg")
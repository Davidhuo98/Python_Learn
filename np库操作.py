from PIL import Image
import numpy as np
im0 = np.array(Image.open('C:/Users/WOOKING/Desktop/R-C.jpg').convert('L'))  #将像素从RGB的三字节形式转变为单一数值形式，这一数值范围为0-255
im1 = 255-im0  #反变换
im2 = (100/255)*im0 +150
im3 = 255*(im1/255)**2
pil_im = Image.fromarray(np.uint8(im1))
pil_im.show()
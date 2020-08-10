from PIL import Image
from resizeimage import resizeimage

with open('test-image.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_width(image, 512)
        image.save('pugizinhopronto.png', image.format)
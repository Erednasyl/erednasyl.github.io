from PIL import Image
from resizeimage import resizeimage
for index in range (0,39):
    img = '/workspace/erednasyl.github.io/pythonJunky/{}.png'
    with open(img.format(209523126+index), 'r+b') as f:
        with Image.open(f) as image:
            #cover = resizeimage.resize_width(image, 50)
            cover = resizeimage.resize_contain(image, [512, 320])
            arquivopronto ='/workspace/erednasyl.github.io/pythonJunky/arquivosprontos/pugizinhopronto{}.png'
            cover.save(arquivopronto.format(index), image.format)
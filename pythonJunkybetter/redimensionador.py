from PIL import Image
img = '/workspace/erednasyl.github.io/pythonJunky/{}.png'
for index in range (0,40):
    with open(img.format(209523126+index), 'r+b') as f :
        with Image.open(f) as image:
            dimensões = [int(image.size[0]*(512/image.size[0])),int(image.size[1]*(512/image.size[1]))]
            cover = image.resize(dimensões)
            arquivofinal = '/workspace/erednasyl.github.io/pythonJunkybetter/done/pugixinho{}.png'
            cover.save(arquivofinal.format(index),image.format)
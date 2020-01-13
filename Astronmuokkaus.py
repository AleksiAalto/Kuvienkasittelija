from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400, 400)) # pitää kuvanlaadun samaisena, kun alkuperäisellä
#img.save('thumbnail.jpg') 

print(img.size)

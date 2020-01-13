from PIL import Image, ImageFilter

#Lisätietoja eri funktioista: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

img = Image.open('./Pokedex/pikachu.jpg')

#blurrattuKuva = img.filter(ImageFilter.BLUR) #tekee blurratun kuva pikazhusta
#blurrattuKuva.save("blur.png", 'png') #tekee siitä tiedostonimen "blur.png" ja tiedostomuodon png
#tässä listattu muutamia toimintoja, mitä kuvatiedostosta on mahdollista saada esille
#print(img.size)
#print(img.format)
#print(img.mode)

#smoothKuva = img.filter(ImageFilter.SMOOTH)
#smoothKuva.save("smooth.png", 'png')

#sharpKuva = img.filter(ImageFilter.SHARPEN)
#sharpKuva.save("sharp.png", 'png')

greyScale = img.convert('L')
greyScale.save("grey.png", 'png')
greyScale.show() # tulostaa ulos kuvan

#print(dir(img)) näkee, mitä kaikkia funktioita on käytössä



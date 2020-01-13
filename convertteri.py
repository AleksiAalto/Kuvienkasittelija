# tämä ohjelma muuntaa kuvat jpg- muodosta png-muotoon
import sys, os
from PIL import Image

# valitse ensimmäinen kansio (=Pokedex), jonka jälkeen toinen (=new)
kuvienKansio = sys.argv[1]
uudetKuvatKansio = sys.argv[2]

# tarkista onko luotu kansiota nimeltä new ja, jos ei ole, luo se
if not os.path.exists(uudetKuvatKansio):
    os.makedirs(uudetKuvatKansio)

# käy pokedex kansio lävitse ja muunna kuvat png muotoon ja tallenna ne new- kansioon
for filename in os.listdir(kuvienKansio):
    img = Image.open(f'{kuvienKansio}{filename}')
    siistittyNimi = os.path.splitext(filename)[0]
    img.save(f'{uudetKuvatKansio}{siistittyNimi}.png', 'png')
    print("Valmista!")


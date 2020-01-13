#pdf muotoon muunnos
import PyPDF2

with open('dummy.pdf', 'rb') as file:
    lukija = PyPDF2.PdfFileReader(file)
    #print(lukija.numPages)
    sivu = lukija.getPage(0)
    sivu.rotateClockwise(90)
    #writer = PyPDF2.PdfFileWriter()
    writer = addPage(sivu)
    with open('kierretty.pdf', 'wb') as uusi_file:
        writer.write(uusi_file)

#pdf muotoon muunnos
import PyPDF2
import sys

#with open('dummy.pdf', 'rb') as file:
    #lukija = PyPDF2.PdfFileReader(file)
    #print(lukija.numPages)
    #sivu = lukija.getPage(0)
    #sivu.rotateClockwise(90)
    #writer = PyPDF2.PdfFileWriter()
    #writer = addPage(sivu)
    #with open('kierretty.pdf', 'wb') as uusi_file:
       # writer.write(uusi_file)

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    yhdista = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        yhdista.append(pdf)
    
    yhdista.write('super.pdf')


pdf_combiner(inputs)
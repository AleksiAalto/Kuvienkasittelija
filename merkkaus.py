import PyPDF2

template = PyPDF2.PdfFileReader(open('dummy.pdf', 'rb'))
merkki = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(merkki.getPage(0))
    output.addPage(page)
    
    with open('merkattufilu.pdf', 'wb') as file:
        output.write(file)
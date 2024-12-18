import PyPDF2, os

pdfFiles = []

for filename in os.listdir('article') :
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
        
pdfFiles.sort(key= str.lower)

pdfWriter = PyPDF2.PdfWriter()

for filename in pdfFiles:
    pdfFileObj = open(f'article\\{filename} ' , 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    for pageNum in range(1 ,len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)
        
        
pdfOutput = open('article\\article.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close
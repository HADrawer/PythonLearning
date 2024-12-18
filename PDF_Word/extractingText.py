import PyPDF2


pdfFileObj = open("pdf_test.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

#pages number

print(len(pdfReader.pages))

#read

pageObj = pdfReader.pages[1]

print(pageObj.extract_text())

pdfFileObj.close()
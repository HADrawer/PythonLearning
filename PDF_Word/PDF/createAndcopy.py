from PyPDF2 import PdfWriter as w

import PyPDF2

#create

pdf = w()
file = open('pdf_file.pdf', "wb")
for i in range(5):
    pdf.add_blank_page(219,297) #a4
pdf.write(file)

#copy 
pdfFile = open("pdf_test.pdf", "rb") 
pdfReader = PyPDF2.PdfReader(pdfFile)

for pageNum in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdf.add_page(pageObj)

pdf.write(file)

file.close
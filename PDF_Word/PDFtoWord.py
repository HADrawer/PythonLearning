from pdf2docx import Converter

pdf_file = 'PDF\\article\\article.pdf'
docx_file = 'Word\\pdf_test_converted.docx'


cv = Converter(pdf_file)
cv.convert(docx_file,start=2,end=6)
cv.close
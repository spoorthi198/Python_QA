import PyPDF2
# reading pdf dta
file = open('sample.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)
pdfData = reader.getPage(0)
print(pdfData.extractText())
data = pdfData.extractText()
file.close()

# looking for text
assert "Mechanics1" in data, 'Not present'
print('it is present')

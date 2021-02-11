import PyPDF4
from PIL import Image

def extrace_info(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF4.PdfFileReader(f)
        info = pdf.getDocumentInfo()
        numOfPages = pdf.getNumPages()

def convertJPGtoPdf(jpg_path, outputName):
    image = Image.open(r"path")
    im = image.convert('RGB')
    im.save(outputName)


if __name__ == '__main__':
    #path = '88538438.pdf'
    #extrace_info(path)
    image1 = Image.open(r'driverlicence_front.jpg')
    image2 = Image.open(r'driverlicence_back.jpg')
    im1 = image1.convert('RGB')
    im2 = image2.convert('RGB')
    im1.save(r'licence1.pdf')
    im2.save(r'licence2.pdf')
    pdf_reader1 = PyPDF4.PdfFileReader('licence1.pdf')
    pdf_reader2 = PyPDF4.PdfFileReader('licence2.pdf')
    pdf_write = PyPDF4.PdfFileWriter()
    pdf_write.addPage(pdf_reader1.getPage(0))
    pdf_write.addPage(pdf_reader2.getPage(0))

    with open('licence.pdf', 'wb') as out:
        pdf_write.write(out)
    
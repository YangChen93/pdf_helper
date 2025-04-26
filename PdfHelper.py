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

def processPDF(pdf_path_1, pdf_path_2):
    pdf_reader1 = PyPDF4.PdfFileReader(pdf_path_1)
    pdf_reader2 = PyPDF4.PdfFileReader(pdf_path_2)
    pdf_write = PyPDF4.PdfFileWriter()
    
    # Add pages from the first PDF
    for page in range(pdf_reader1.getNumPages()):
        pdf_write.addPage(pdf_reader1.getPage(page))
    
    # Add pages from the second PDF
    for page in range(pdf_reader2.getNumPages()):
        pdf_write.addPage(pdf_reader2.getPage(page))
    
    # Save the combined PDF
    with open('combined.pdf', 'wb') as out:
        pdf_write.write(out)

def processJPG(jpg_path_1, jpg_path_2):
    image1 = Image.open(jpg_path_1)
    image2 = Image.open(jpg_path_2)

if __name__ == '__main__':
    print("This tool only support PDF and JPG, now please make the choice:\n")
    isPdf = input("Is it PDF file: yes/no?")
    if (isPdf == "yes"):
        pathPdf1 = input("Enter the path of first pdf file:")
        pathPdf2 = input("Enter the path of second pdf file:")
        processPDF(pathPdf1, pathPdf2)
    else:
        pathJpg1 = input("Enter the path of first jpg file:")
        pathJpg2 = input("Enter the path of second jpg file:")
        processJPG(pathJpg1, pathJpg2)

    
    #extrace_info(path)
    #image1 = Image.open(r'driverlicence_front.jpg')
    #image2 = Image.open(r'driverlicence_back.jpg')
    #im1 = image1.convert('RGB')
    #im2 = image2.convert('RGB')
    #im1.save(r'licence1.pdf')
    #im2.save(r'licence2.pdf')
    #pdf_reader1 = PyPDF4.PdfFileReader('licence1.pdf')
    #pdf_reader2 = PyPDF4.PdfFileReader('licence2.pdf')
    #pdf_write = PyPDF4.PdfFileWriter()
    #pdf_write.addPage(pdf_reader1.getPage(0))
    #pdf_write.addPage(pdf_reader2.getPage(0))

    #with open('licence.pdf', 'wb') as out:
    #    pdf_write.write(out)
    
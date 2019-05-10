from PyPDF2 import PdfFileMerger

def pdf_merge(filename):
    merger = PdfFileMerger()

    pdf_cover = open('pdf/'+filename + '_cover.pdf', 'rb')
    merger.append(pdf_cover)

    pdf_body = open('pdf/'+filename + '_body.pdf', 'rb')
    merger.append(pdf_body)

    outfile = open('pdf/'+filename + '-transcript.pdf', 'wb')
    merger.write(outfile)

    pdf_cover.close()
    pdf_body.close()
    outfile.close()


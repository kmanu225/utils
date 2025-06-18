from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["pdf1.pdf", "pdf2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
import fitz

pdf = fitz.open("Resume.pdf")

for i, page in enumerate(pdf):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    pix.save(f"page_{i+1}.png")
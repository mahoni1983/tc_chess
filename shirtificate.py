"""In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate
in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text."""

from fpdf import FPDF

text_on_top = "CS50 Shirtificate"

name = input('Name: ')


pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 50)
pdf.cell(0, 30, "CS50 shirtificate", align="C")
pdf.ln(50)

# Rendering logo:
# pdf.image("shirtificate.png", 10, 8, 33)
pic = 'https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png'
# pdf.image("shirtificate.png", w=pdf.epw, keep_aspect_ratio=True)
pdf.image(pic, w=pdf.epw, keep_aspect_ratio=True)
# Setting font: helvetica bold 15
# pdf.set_font("helvetica", "B", 15)
# Moving cursor to the right:
# pdf.cell(80)
# Printing title:
# pdf.cell(30, 10, "Title", border=1, align="C")
# Performing a line break:

pdf.set_font("helvetica", "B", 40)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, -200, name, align="C")
pdf.set_auto_page_break(False)
pdf.output("shirtificate.pdf")

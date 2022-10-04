#FPDF2 Documentation: https://pyfpdf.github.io/fpdf2/Tutorial.html

#import fpdf2
#get user's name
#print name onto shirt "[NAME] took CS50"
#output to a PDF that is:
    #portrait, A4, has "CS50 Shirtificate" at the top and centred horizontally, shirt should be centred horizontally, name should be in white text


from fpdf import FPDF
import sys

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32) # Set font
        self.cell(80) # Move cursor to right by changing only the x of the cell
        self.cell(30, 10, "CS50 Shirtificate", align="C") # Print title in cell/box at x=30mm y=10mm away from cursor? Text centre aligned within box
        self.ln(150) # New line with gap of 150(mm)?

pdf = PDF() # Assign "pdf to FPDF class
pdf.add_page() # Add a page
pdf.image("shirtificate.png", 10, 107.1, pdf.epw) # Add shirt image at x10mm (margin), y107.1 (allows bottom of image to align with bottom of page) width = full page width
name = input ("Name: ") # Name input
pdf.set_text_color(255) # Changes text colour to white
pdf.set_font("helvetica", "B", 16) # Set font
pdf.cell(90) # Move cursor to right by changing x of cell
pdf.cell(15, 10, f"{name} took CS50", align="C") # Print text in cell/box at 15mm x 10mm away from cursor? Text centre aligned within box
pdf.output("shirtificate.pdf") # Output pdf file
sys.exit() # Exit the program
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 60, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

    def add_image(self):
        # Rendering logo:
        self.image("shirtificate.png", x=5, y=70, w=200)

    def print_shirt(self, name):
        self.add_image()
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        # Printing title:
        self.cell(0, 200, name + " took CS50", border=0, align="C")


def main():

    name = input("Name: ")

    # Instantiation of inherited class
    pdf = PDF()
    pdf.add_page()
    pdf.print_shirt(name)
    pdf.output(name + " CS50 shirtificate.pdf")

if __name__ == "__main__":
    main()
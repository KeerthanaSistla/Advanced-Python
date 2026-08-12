from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font(family='Times', size=24, style='B')
pdf.cell(w=100, h=80, txt='Flatmates Bill', border=1, ln=1, align='C')
pdf.cell(w=100, h=40, txt='Period', border=1)
pdf.cell(w=150, h=40, txt='March 2021', border=1, ln=1)

pdf.output("2. Flatmates' Bill\\bill.pdf")
from fpdf import FPDF

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (
            self.days_in_house + flatmate2.days_in_house
        )
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=80, txt='Flatmates Bill', border=1, ln=1, align='C')
        pdf.cell(w=100, h=40, txt='Period', border=1)
        pdf.cell(w=150, h=40, txt='March 2021', border=1, ln=1)

        pdf.output("2. Flatmates' Bill\\bill.pdf")


the_bill = Bill(amount=120, period="March 2021")

john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print(john.pays(bill=the_bill, flatmate2=mary))
print(mary.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="bill.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)
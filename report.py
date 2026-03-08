import csv
from fpdf import FPDF
from datetime import datetime

# --------------------
# Read Data
# --------------------
records = []
total = 0

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        records.append(row)
        total += int(row[2])

average = total / len(records)

# --------------------
# Create PDF
# --------------------
pdf = FPDF()
pdf.add_page()

# ---------- HEADER ----------
pdf.set_font("Arial", "B", 20)
pdf.cell(0, 10, "CODTECH AUTOMATED REPORT", ln=True, align="C")

pdf.set_font("Arial", "", 12)
date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
pdf.cell(0, 8, f"Generated On: {date}", ln=True, align="R")

pdf.ln(10)

# ---------- REPORT TITLE ----------
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Sales Analysis Report", ln=True)

pdf.ln(5)

# ---------- TABLE HEADER ----------
pdf.set_font("Arial", "B", 12)

pdf.cell(60, 10, "Name", border=1, align="C")
pdf.cell(70, 10, "Product", border=1, align="C")
pdf.cell(50, 10, "Amount", border=1, align="C")
pdf.ln()

# ---------- TABLE DATA ----------
pdf.set_font("Arial", "", 12)

for row in records:
    pdf.cell(60, 10, row[0], border=1)
    pdf.cell(70, 10, row[1], border=1)
    pdf.cell(50, 10, row[2], border=1, align="R")
    pdf.ln()

pdf.ln(10)

# ---------- SUMMARY ----------
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Summary", ln=True)

pdf.set_font("Arial", "", 12)
pdf.cell(0, 8, f"Total Sales : {total}", ln=True)
pdf.cell(0, 8, f"Average Sales : {average:.2f}", ln=True)
pdf.cell(0, 8, f"Total Records : {len(records)}", ln=True)

pdf.ln(15)

# ---------- FOOTER ----------
pdf.set_font("Arial", "I", 10)
pdf.cell(0, 10, "Generated automatically using Python & FPDF", align="C")

# Save PDF
pdf.output("report.pdf")

print("Professional Report Generated Successfully!")
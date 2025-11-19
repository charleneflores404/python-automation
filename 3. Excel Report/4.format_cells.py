from openpyxl import load_workbook
from openpyxl.styles import Font
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths for input and output files
input_path = os.path.join(script_dir,'report.xlsx')
output_path = os.path.join(script_dir, 'report_january.xlsx')

wb = load_workbook(input_path)
sheet = wb['Report']

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save(output_path)
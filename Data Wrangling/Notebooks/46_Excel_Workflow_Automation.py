# Import Libraries
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch
import os


# Data
data = {
"Asset Name": ['Asset 1', 'Asset 2'],
"Month 1": [15, 20],
"Month 2": [5, 35],
}

# Dataframe
df = pd.DataFrame(data)

# Create and save an Excel file
file_path = os.path.abspath('excel_python.xlsx')  # Get absolute path
workbook = Workbook()
sheet = workbook.active

for row in dataframe_to_rows(df, index = False, header = True):
	sheet.append(row)


workbook.save(filename=file_path)  # Save workbook


# Open the file in Excel
xl = Dispatch('Excel.Application')
xl.Visible = True  # Make Excel visible
xb = xl.Workbooks.Open(file_path)  # Open the saved file
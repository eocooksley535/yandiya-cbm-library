"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This python script was created to test the viability of using excel instead of CSVs (at least for the MVP)

This script allows the user to input the partNo of the product they wish to get the infomation of.

"""

import openpyxl

yandiya_db = openpyxl.load_workbook(
    '.excel_db_test\yandiya-db.xlsx')

# print(yandiya_db.sheetnames)

records_table = yandiya_db.active

# print(records_table)

# ask user for input, iterate over column PartNo or "A" , check if input value is equal to any values in column
parameters = str(input(
    "Please enter the PartNo you wish to seach for "))

partNo = records_table['A']

for cell in records_table:
    if {cell.value} == parameters:
        print("Success!!!!")

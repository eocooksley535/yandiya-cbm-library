"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function
and will most likely be removed or archived in the final version

It is a simple CLI python application that allows the user to 
search a database of yandiya's products stored on an excel doc.

It was created to test the viability for using an excel doc.

"""

import openpyxl

path - "product-details (DATA INPUT).xlsx"
workbook_db = openpyxl.load_workbook(path)
product_sheet = workbook_db.sheet_by_name('Sheet1')

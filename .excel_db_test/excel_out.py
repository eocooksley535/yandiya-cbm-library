"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function
and will most likely be removed or archived in the final version

It is a simple CLI python application that prints out the 
values from an excel doc 

It was created to test the viability for using an excel doc.

"""

import openpyxl

theFile = openpyxl.load_workbook(
    '.excel_db_test\product-details (DATA INPUT).xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))


for sheet in allSheetNames:
    print("Current sheet name is {}" .format(sheet))
    currentSheet = theFile[sheet]
    # print(currentSheet['B4'].value)

    # print max numbers of wors and colums for each sheet
    # print(currentSheet.max_row)
    # print(currentSheet.max_column)

    for row in range(1, currentSheet.max_row + 1):
        # print(row)
        for column in "ABCDEF":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            # print(cell_name)
            print("cell position {} has value {}".format(
                cell_name, currentSheet[cell_name].value))

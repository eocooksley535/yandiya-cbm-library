"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script the yandiya-db.xslx (excel file) is required

"""


import openpyxl


def searching_product(parameters):
    yandiya_db = openpyxl.load_workbook(
        '.main\yandiya-db.xlsx')
    records_table = yandiya_db.active

    if len(parameters) == 13:
        search_column = records_table['B']  # barcode
    elif len(parameters) == 5:
        search_column = records_table['C']  # sku
    else:
        search_column = records_table['A']  # partNo

    for cell in search_column:
        if cell.value == parameters:
            reqData = records_table[cell.row]
            break

    output = []
    for cell in reqData:
        output.append(cell.value)

    return output


def cbm_calculations(parameters: list, itemQuantity: int):
    # multiple dimensions together and then by the quanity to get CBM
    #cbmCalculated = itemQuantity
    # for i in range(len(itemDimensions)):
    #    cbmCalculated = cbmCalculated * itemDimensions[i]
    # return cbmCalculated
    return 0


def headings():
    return 0

"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script the yandiya-db.xslx (excel file) is required

"""


import openpyxl
import time
import timeit

from openpyxl import Workbook


def extrl(parameters, records_table: Workbook.active):
    if len(parameters) == 5:
        return records_table['C']  # sku
    elif len(parameters) == 13:
        return records_table['B']  # barcode
    else:
        return records_table['A']  # partNo


def searching_product(parameters):
    yandiya_db = openpyxl.load_workbook(
        '.main\yandiya-db.xlsx')
    records_table = yandiya_db.active

    search_column = extrl(parameters, records_table)

    timeit.repeat("for ")

    for cell in search_column:
        if cell.value == parameters:
            reqData = records_table[cell.row]
            break

    output = []
    for cell in reqData:
        output.append(cell.value)

    return output


def calculate(parameters: list, itemQuantity: int):
    # multiple dimensions together and then by the quanity to get CBM
    #cbmCalculated = itemQuantity
    # for i in range(len(itemDimensions)):
    #    cbmCalculated = cbmCalculated * itemDimensions[i]
    # return cbmCalculated
    return 0


def headings():
    return ['partNo', 'barcode', 'sku', 'productTitle', 'pWidth', 'pHeight', 'pDepth', 'icWidth', 'icHeight',
            'icDepth', 'icWeight', 'icQty', 'ocWidth', 'ocHeight', 'ocDepth', 'ocWeight', 'ocQty']
    # 14 , 13, 12

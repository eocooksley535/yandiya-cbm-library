"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script all the csv files are required also.
These includes: product-details.csv, pallet-types.csv, parcel-types.csv & delivery-costs.csv

"""


import openpyxl


def searching_product(parameters):
    yandiya_db = openpyxl.load_workbook(
        '.excel_db_test\yandiya-db.xlsx')

    records_table = yandiya_db.active
    partNo = records_table['A']
    #barcode = records_table['B']
    #sku = records_table['C']

    for cell in partNo:
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

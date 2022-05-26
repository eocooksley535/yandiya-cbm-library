"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script all the csv files are required also.
These includes: product-details.csv, pallet-types.csv, parcel-types.csv & delivery-costs.csv

"""

import csv
import pandas as pd
import numpy as np

# select and add to array OC W, H & D from row that contains searched values


def searching_product(item):
    inventoryDf = pd.read_csv('product_details.csv')
    selectedRow = inventoryDf.loc[inventoryDf["partNo"] == item]
    return selectedRow


def cbm_calculations():  # itemDimensions: tuple, itemQuantity: int):
    # multiple dimensions together and then by the quanity to get CBM
    #cbmCalculated = itemQuantity
    # for i in range(len(itemDimensions)):
    #    cbmCalculated = cbmCalculated * itemDimensions[i]
    # return cbmCalculated
    return 0

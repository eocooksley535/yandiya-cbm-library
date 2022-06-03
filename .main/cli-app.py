"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is a simple CLI python application that allows the user to 
interact with the yandiya-cbm-library.

It was created to make the initial development of 
the yandiya-cbm-library easier to test

later versions of this repository will 
include an Odoo module and WebUI to interact with the yandiya-cbm-library

"""
import cbmcalculator

parameters = input("Whats the product number, barcode or sku of the item? ")
productQuantity = int(input(
    "\nWhat's the quantity of the items that you need? "))

inWarehouse = cbmcalculator.searching_product(parameters)
cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

print("The CBM is ", cbm[0], ", the total weight is ",
      cbm[1], " the items will be sent in a ", cbm[2])

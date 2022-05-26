"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT apart of the yandiya-cbm-library

It is a simple CLI python application that allows the user to 
interact with the yandiya-cbm-library.

It was created to make the initial development of 
the yandiya-cbm-library easier to test

"""
import cbmcalculator

productCode = input("Whats the product code of the item?")
productQuantity = input(
    "\nWhat's the quantity of the items that you need.")

inInventory = cbmcalculator.searching_product(productCode)
print(inInventory)

"""
cbm = cbmcalculator.cbm_calculations(inInventory, productQuantity)

print("The CBM of ", productQuantity,
      " ", productCode, " is ", cbm)

"""

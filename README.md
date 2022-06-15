# Yandiya CBM Library

#### Current Version V0.1

- a python library written for Yandiya Technologies Ltd during my T Level Industry Placement.
- currently meets 3 out of 5 of the milestones listed in the proposal

## Description

The Python library is being written for Yandiya Technologies Ltd. Its purpose is to allow their employees to easily calculate the CBM (Cubic Meter) of their products the library takes user input of which of Yandiya's products they are packaging and it calculates the CBM, whether to use a pallet or parcel, if appicable which type of pallet would be best to use and the cost of delivery.

## Getting Started

### Dependencies

#### Prerequisites

- [Python 3.10](https://www.python.org/downloads/) - older versions are likely to work as the code base doesn't utalize any python 3.10 specific features but this can't be ensured as no previous versions have been tested
- [yandiya-db.xlsx](https://github.com/elvybean/yandiya-cbm-library/blob/main/.main/yandiya-db.xlsx) - excel file that contains all the data required for the cbm library to function, this is located in the .main folder of the repo

#### Libraries

[openpyxl](https://pypi.org/project/openpyxl/) - which can be installled via pip once in the same directory python

```
pip install openpyxl
```

OR if the py global variable is enabled the following line can be used as an alternative

```
py -m pip install openpyxl
```

#### OS version

Developed and tested on Windows 10 Pro 21H1 - has not been tested on other versions of Windows (7, 8, 8.1 or 11) or Windows 10 (21H2 +) but there is no reason for there to issue.

### Installing

```
This README.md section is unfinshed
```

### Executing program

```
This README.md section is unfinshed
```

## Potential Future Adddions

- Odoo Module to interact with the python library
- Web UI to interact with the python library - using pyscript
- pip package to simlify instillation of library

## Authors

Contributors names and contact info

Elvis Obero-Atkins
[LinkedIn](www.linkedin.com/in/elvisoberoatkins)

## Version History

- 0.1
  - Accesses Yandiya's product data from yandiya-db.xlsx
  - Library takes user input for PartNo, sku or barcode
  - Searches excel file for the product the user is looking for
  - Calculates CBM for the product based on it's dimensions and quantity of the product
  - Calculates based on the total weight weather to send products via pallets or parcel
  - Has basic error messages in the event the search returns no values

## License

This project is licensed under the [MIT Lisence](https://choosealicense.com/licenses/mit/)

## Acknowledgments

Inspiration, code snippets, etc.

- [cbmcalculator.com for the Web UI inspiration](https://www.cbmcalculator.com/)
- [Dominique Pizzie&#39;s Gist for the README.md Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)

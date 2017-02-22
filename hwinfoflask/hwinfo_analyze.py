"""
"""

import csv
from collections import OrderedDict
import openpyxl

from . import gpu
from . import cpu
from . import voltage
from . import helpers

def main(filename):
    with open(filename, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        csv_data = {header: [] for header in headers}
        data_dict = {header: [] for header in headers}
        for row in reader:
            for header in headers:
                cell = row[header]
                if cell != header:
                    try:
                        csv_data[header].append(float(cell))
                    except ValueError:
                        csv_data[header].append(cell)


        message_dict = OrderedDict()
        message_dict["Cpu"] = cpu.main(csv_data)
        message_dict["Gpu"] = gpu.main(csv_data)
        message_dict["Voltage"], graph_name = voltage.main(csv_data)
        return message_dict, graph_name


if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename
    filename = ""
    while not filename.lower().endswith("csv"):
       filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    main(filename)

'''
'''

import csv
from collections import OrderedDict
import openpyxl

import gpu
import cpu
import voltage
import helpers

def main(filename):
    with open(filename, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        csv_data = {header: [] for header in headers}
        for row in reader:
            for header in headers:
                cell = row[header]
                if cell != header:
                    try:
                        csv_data[header].append(float(cell))
                    except ValueError:
                        csv_data[header].append(cell)

        message = OrderedDict()


        #CPU stuff
        message["Cpu"] = cpu.main(csv_data)

        #GPU stuff
        message["Gpu"] = gpu.main(csv_data)

        #voltages
        message["Voltage"] = voltage.main(csv_data)

        #Drive stuff
        #drive activity
        #param_names = ["Total Activity [%]"]
        #trigger_value = 65
        #message += helpers.check_max_parameter([param_names, 65])

        #cpu overclocked
        #amd
        #intel

    # add max recorded value to warning message?
    #
        return message



if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename
    filename = ""
    while not filename.lower().endswith("csv"):
       filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

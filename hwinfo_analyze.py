'''
'''

import csv
<<<<<<< HEAD
from collections import OrderedDict
import openpyxl
=======
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69

import gpu
import cpu
import voltage
import helpers

def main(filename):
    with open(filename, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

<<<<<<< HEAD
        csv_data = {header: [] for header in headers}
=======
        data_dict = {header: [] for header in headers}
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69
        for row in reader:
            for header in headers:
                cell = row[header]
                if cell != header:
                    try:
<<<<<<< HEAD
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
=======
                        data_dict[header].append(float(cell))
                    except ValueError:
                        data_dict[header].append(cell)

        message = ''

        #CPU stuff
        message += cpu.main(data_dict)

        #GPU stuff
        message += gpu.main(data_dict)

        #voltages
        message += voltage.main(data_dict)
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69

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

<<<<<<< HEAD


=======
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69
if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename
    filename = ""
    while not filename.lower().endswith("csv"):
<<<<<<< HEAD
       filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
=======
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    print(main(filename))
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69

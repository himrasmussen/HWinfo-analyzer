'''
Helper functions.
'''


import shutil
import openpyxl

#TODO: Header to Letters

def check_max_parameter(parameter, csv_data, max_value=1):
    try:
        if max(csv_data[parameter]) >= max_value:
            return "Max " + raise_warning(
                                    parameter,
                                    report_value = max(csv_data[parameter])
                                    )
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

def check_min_parameter(parameter, csv_data, min_value=1):
    try:
        if min(csv_data[parameter]) <= min_value:
            return "Min " + raise_warning(
                                    parameter,
                                    report_value = min(csv_data[parameter])
                                    )
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

def check_yes_parameter(parameter, csv_data):
    try:
        if "Yes" in csv_data[parameter]:
            return raise_warning(parameter, report_value="Yes")
    except KeyError:
        return "No such parameter ({})\n".format(parameter)
    else:
        return ''

'''
"The ripple limits, according to the ATX specification,
are 120mV for the +12V and -12V rails,
and 50mV for the remaining rails (5V, 3.3V and 5VSB).
'''

def check_ripple(parameter, csv_data):
    max_ripple_values = {
                            "+12V [V]": .12,
                            "+5V [V]": .05,
                            "+3.3V [V]": .05
    }
    count = 1

    try:
        avg = sum(csv_data[parameter]) / len(csv_data[parameter])
    except KeyError:
        return "KeyError: {}\n".format(parameter)
    else:
        for i in csv_data[parameter]:
            if abs(i - avg) > max_ripple_values[parameter]:
                count += 1

        if len(csv_data[parameter]) / 100 * 80 <= count:
            return "Ripple on {}.\n".format(parameter)




def raise_warning(parameter, report_value=''):
    return "{0}: {1}\n".format(parameter, report_value)

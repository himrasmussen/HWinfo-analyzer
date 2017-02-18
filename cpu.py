'''
'''

import helpers

def main(csv_data):
    message = ''

    #thermal throttling
    param_names = ["Core #0 Thermal Throttling [Yes/No]",
                   "Core #1 Thermal Throttling [Yes/No]",
                   "Core #2 Thermal Throttling [Yes/No]",
                   "Core #3 Thermal Throttling [Yes/No]"]
    for parameter in param_names:
        message += helpers.check_yes_parameter(parameter, csv_data)

    #critical temp
    param_names = ["Core #0 Critical Temperature [Yes/No]",
                   "Core #1 Critical Temperature [Yes/No]",
                   "Core #2 Critical Temperature [Yes/No]",
                   "Core #3 Critical Temperature [Yes/No]"]
    for parameter in param_names:
        message += helpers.check_yes_parameter(parameter, csv_data)


    #temp
    param_names = ["Core #0 [°C]",
    	           "Core #1 [°C]",
                   "Core #2 [°C]",
                   "Core #3 [°C]"]
    try:
        data = [i for parameter in param_names for i in csv_data[parameter]]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += "Max cpu core temp: {}\n".format(round(max(data)))

    #Vcore
    parameter = "Vcore [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key.format(parameter)
    else:
        message += "Vcore min: {}\n".format(min(data))
        message += "Vcore max: {}\n".format(max(data))

    param_names = ["Core #0 Clock [MHz]",
                   "Core #1 Clock [MHz]",
                   "Core #2 Clock [MHz]",
                   "Core #3 Clock [MHz]"]

    for parameter in param_names:
        try:
            data = csv_data[parameter]
        except KeyError:
            message += helpers.no_key.format(parameter)
        else:
            message += "{0} average MHz: {1}\n".format(parameter, round(sum(data)/len(data)))


    return helpers.sort_message(message)

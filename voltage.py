'''
Voltage checks.
'''



import helpers
#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''


    parameter = "+3.3V [V]"
    try:
        csv_data[parameter]
    except KeyError:
        message += "Key error: {}".format(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=3.47)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=3.14)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+5V [V]"
    try:
        csv_data[parameter]
    except KeyError:
        message += "Key error: {}".format(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=5.25)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=4.75)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+12V [V]"
    try:
        csv_data[parameter]
    except KeyError:
        message += "Key error: {}".format(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=12.60)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=11.40)
        #message += helpers.check_ripple(parameter, csv_data)


    return message

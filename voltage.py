'''
Voltage checks.
'''

import helpers
#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''

    parameter_names = None
    parameter = "+3.3V [V]"
    message += helpers.check_max_parameter([parameter], csv_data, max_value=3.47)
    message += helpers.check_min_parameter([parameter], csv_data, min_value=3.14)

    parameter = "+5V [V]"
    message += helpers.check_max_parameter([parameter], csv_data, max_value=5.25)
    message += helpers.check_min_parameter([parameter], csv_data, min_value=4.75)

    parameter = "+12V [V]"
    message += helpers.check_max_parameter([parameter], csv_data, max_value=12.60)
    message += helpers.check_min_parameter([parameter], csv_data, min_value=11.40)



    return message

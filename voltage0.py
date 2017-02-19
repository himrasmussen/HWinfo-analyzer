'''
Voltage checks.
'''



import helpers
import graph_maker

#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''


    parameter = "+3.3V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=3.47)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=3.14)
        graph_maker.draw_chart(data, parameter)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+5V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=5.25)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=4.75)
        graph_maker.draw_chart(data, parameter)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+12V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=12.60)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=11.40)
        graph_maker.draw_chart(data, parameter)
        #message += helpers.check_ripple(parameter, csv_data)

    graph_maker.draw_multiple_lines([
                                    csv_data["+3.3V [V]",
                                    csv_data["+5V [V]"],
                                    csv_data["+12V [V]"]
                                )



    return helpers.sort_message(message)

'''
'''



from . import helpers
from . import graph_maker

#TODO: So you'd need vcore, dram voltage, anything with a + in front of it such as +5v

def main(csv_data):
    message = ''
    rail_data = {
                    "3.3v": 0,
                    "5v":   0,
                    "12v":  0
                }


    parameter = "+3.3V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
        del rail_data["3.3v"]
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=3.47)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=3.14)
        rail_data["3.3v"] = helpers.make_rel_dev_list(csv_data["+3.3V [V]"])
        #image_path = graph_maker.draw_chart(data, parameter)
        #message += helpers.html_formatted_image(image_path)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+5V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
        del rail_data["5v"]
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=5.25)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=4.75)
        rail_data["5v"] = helpers.make_rel_dev_list(csv_data["+5V [V]"])

        #image_path = graph_maker.draw_chart(data, parameter)
        #message += helpers.html_formatted_image(image_path)
        #message += helpers.check_ripple(parameter, csv_data)

    parameter = "+12V [V]"
    try:
        data = csv_data[parameter]
    except KeyError:
        message += helpers.no_key(parameter)
        del rail_data["12v"]
    else:
        message += helpers.check_max_parameter(parameter, csv_data, max_value=12.60)
        message += helpers.check_min_parameter(parameter, csv_data, min_value=11.40)
        rail_data["12v"]  = helpers.make_rel_dev_list(csv_data["+12V [V]"])

    for k,v in rail_data.items():
        print(k, v[0:2])
    graph_path = graph_maker.draw_chart(rail_data)


    return helpers.sort_message(message), graph_path

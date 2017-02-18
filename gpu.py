'''
Tuples for GPU related checks.
'''
import random
import helpers

def main(csv_data):
    message = ''

    #memory error
    parameters = ["GPU Memory Errors []"]
    try:
        message += helpers.check_yes_parameter(parameter, csv_data)
    except KeyError:
        helpers.no_key(parameter)


    #g12v rail failiure
    #VR VIN (ATX +5V) [V] ?
    parameter = ["GPU VRM Voltage In (VIN/+12V) [V]", "VR VIN (ATX +12V) [V]"]
    for parameter in parameters:
        try:
            message += helpers.check_min_parameter(parameter, csv_data, 11.40)
            message += helpers.check_max_parameter(parameter, csv_data, 12.60)
        except KeyError:
            helpers.no_key(parameter)

    #Usage
    parameters = ["GPU Utilization [%]", "GPU D3D Usage [%]"]
    for parameter in parameters:
        try:
            data = csv_data[parameter]
        except KeyError:
            message += helpers.no_key(parameter)
        else:
            message += "{0} average usage: {1}\n".format(
                                                    round(sum(data)/len(data)),
                                                    parameter
                                                    )

    #Temperature
    parameters = ["GPU Thermal Diode [°C]",
                 "GPU Temperature (HW) [°C]",
                 "GPU Temperature [°C]"]
    for parameter in parameters:
        try:
            data = csv_data[parameter]
        except KeyError:
            message += helpers.no_key(parameter)
        else:
            message += "{} max: {}\n".format(parameter, max(data))
            message += "{} sample: {}\n".format(
                                        parameter,
                                        random.sample(data, min(len(data), 20)))

    #Average hz
    parameters = ["GPU Clock [MHz]", "GPU Video Clock [MHz]"]
    for parameter in parameters:
        try:
            message += "{0} average: {1}\n".format(
                                                parameter,
                                                round(sum(data) / len(data)))
        except KeyError:
            message += helpers.no_key(parameter)


    return helpers.sort_message(message)

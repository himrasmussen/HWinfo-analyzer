from matplotlib import pyplot as plt
import os

from flask import url_for
# Plot data.
#
#
def draw_chart(data_in):
    print(os.getcwd())
    GRAPH_FOLDER_PATH = ASSET_FOLDER = os.path.join(
                                                    "hwinfoflask",
                                                    "graphs"
                                                    )
    fig = plt.figure(dpi=128, figsize=(10, 6))
    if "12v" in data_in.keys():
        plt.plot(data_in["12v"], c='blue', label="12V")
    if "5v" in data_in.keys():
        plt.plot(data_in["5v"], c='green', label="5V")
    if "3.3v" in data_in.keys():
        plt.plot(data_in["3.3v"], c='red', label="3.3V")
    plt.title("Deviation from rail average", fontsize=24)
    plt.xlabel('Red - 3.3v  Green - 5v  Blue - 12v', fontsize=16)
    plt.ylabel('Volts', fontsize=16)
    plt.tick_params(axis='x', which='major', labelsize=16)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.yticks([-.120, -.05, 0, .05, .120])
    #plt.show()
    file_number =  len(os.listdir(GRAPH_FOLDER_PATH)) + 1
    #file_number = 1
    #file_number = os.listdir(destination).

    file_name = "{0}.png".format(str(file_number))
    file_path = os.path.join(GRAPH_FOLDER_PATH, file_name)
    plt.savefig((file_path), bbox_inches='tight')
    plt.close()

    return file_name

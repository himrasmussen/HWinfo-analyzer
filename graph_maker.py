from matplotlib import pyplot as plt
import os
# Plot data.
#
#


def draw_chart(data_in, title):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(data_in, c='red')
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Voltage", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    #plt.show()
    #file_number =  int(len(os.listdir("graphs")) / 3, 0) + 1
    file_number = 9001
    file_name = "{0}_{1}.png".format('_'.join(title.split()), str(file_number))
    file_path = os.path.abspath(os.path.join('graphs', file_name))
    plt.savefig((file_path), bbox_inches='tight')
    plt.close()
    return file_path

def draw_multiple_lines(data_in):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(data_in[2], c='blue', label="12V")
    plt.plot(data_in[1], c='green', label="5V")
    plt.plot(data_in[0], c='red', label="3.3V")
    plt.title("Deviation from rail average in mV", fontsize=24)
    plt.xlabel('Red - 3.3v  Green - 5v  Blue - 12v', fontsize=16)
    plt.ylabel('mV', fontsize=16)
    plt.tick_params(axis='x', which='major', labelsize=16)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.yticks([-0.12, -0.05, 0, 0.05,0.12])
    #plt.show()
    #file_number =  int(len(os.listdir("graphs")) / 3, 0) + 1
    #file_number = os.listdir(destination).
    file_number = 3
    file_name = "Tripple_{0}.png".format(str(file_number))
    file_path = os.path.abspath(os.path.join('graphs', file_name))
    plt.savefig((file_path), bbox_inches='tight')
    plt.close()

    return file_path

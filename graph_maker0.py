from matplotlib import pyplot as plt
import os
# Plot data.

def draw_chart(data_in, title):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(data_in, c='red')
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Voltage", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    #plt.show()
    file_number =  int(len(os.listdir("graphs")) / 3, 0) + 1
    file_name = "{0}_{1}.png".format(title, str(file_number))
    plt.savefig(os.path.join('graphs', file_name), bbox_inches='tight')


def draw_multiple_lines(data_in):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(data_in[0], c='red', label="3.3V")
    plt.plot(data_in[1], c='green', label="5V")
    plt.plot(data_in[2], c='blue', label="12V")
    plt.title("Relative dif in %", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    #plt.show()
    #file_number =  int(len(os.listdir("graphs")) / 3, 0) + 1
    file_number = 1
    file_name = "Tripple_{0}.png".format(str(file_number))
    plt.savefig(os.path.join('graphs', file_name), bbox_inches='tight')

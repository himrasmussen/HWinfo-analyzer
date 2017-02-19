from matplotlib import pyplot as plt

def draw_multiple_lines(data_in):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    if "3.3v" in data_in.keys():
        plt.plot(data_in["3.3v"], c='red', label="3.3V")
    if "5v" in data_in.keys():
        plt.plot(data_in["5v"], c='green', label="5V")
    if "12v" in data_in.keys():
        plt.plot(data_in["12v"], c='blue', label="12V")
    plt.title("Deviation from rail average in mV", fontsize=24)
    plt.xlabel('Red - 3.3v  Green - 5v  Blue - 12v', fontsize=16)
    plt.ylabel('mV', fontsize=16)
    plt.tick_params(axis='x', which='major', labelsize=16)
    plt.tick_params(axis='y', which='major', labelsize=14)
    plt.yticks([-0.12, -0.05, 0, 0.05,0.12])
    plt.show()


rail_data = {
            "3.3v": [0.04, 0.03],
            "5v": [0.04, -0.05],
            "12v": [0.11, -0.03]
            }

rail_data = {
            "3.3v": [0.04, 0.03],
            "5v": [0.04, -0.05],
            }

draw_multiple_lines(rail_data)

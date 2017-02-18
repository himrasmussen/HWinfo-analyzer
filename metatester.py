from helpers import sort_message

message = "No data: GPU Memory Errors []\nNo data: GPU VRM Voltage In (VIN/+12V) [V]\nNo data: GPU VRM Voltage In (VIN/+12V) [V]\nNo data: GPU Utilization [%]\nNo data: GPU Thermal Diode [C]\nGPU avg hz: 675.2647058823529\n"
for line in sort_message(message):
    print(line)

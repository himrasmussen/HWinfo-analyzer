import os
import csv

with open("uploads\\0.csv") as f:
    reader = csv.DictReader(f)
    headers = next(reader)
    column_dict = {header: [] for header in headers}

    for row in reader:
        for header in headers:
            try:
                column_dict[header].append(float(row[header]))
            except ValueError:
                column_dict[header].append(row[header])

    for k, v in column_dict.items():
        print(k, str(type(v[6])))

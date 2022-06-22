import time
import datetime
import csv

def module_status(input):
    for count, ele in enumerate(input):
        if (ele == "M"):
            module_status = input[count+1:count+8]
            return module_status

rows    = []
t       = []
data    = []

with open('data.csv', newline='') as csvfile:
    csv_object = csv.reader(csvfile, delimiter = ',', quotechar='|')
    total_rows = 1
    for row in csv_object:
        rows.append(row)
    lastrow = csv_object.line_num
    for row in rows: # change this to only read the last 30 rows or so...
        t.append(row[0])
        data.append(row[1])
import time
import datetime
import csv

def timestamp(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time)
    
with open('data.csv', newline='') as csvfile:
    read = csv.reader(csvfile, delimiter = ',',  quotechar = '|')
    for row in read:
        if(row[0:3] == 1655):
            print(timestamp(row))
        
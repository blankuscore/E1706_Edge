import altair as alt
from vega_datasets import data
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import datetime
import pandas as pd
import csv

t = [1.1] #initialize t as a float
surge_count = []
tov_count = []

def html_chart():
    chart = alt.Chart(data.cars.url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N'
    )
    chart.save('chart.html', embed_options={'actions': False})

def timestamp(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time)

def csv_read():
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            t.append(timestamp(float(row[0])))
            surge_count.append(row[1])
        #print(t[2:len(t)])
        #x_axis = mdates.date2num(t[2:len(t)])
        #print(x_axis)
        #y_axis = surge_count[1:len(surge_count)]
        
    """ 
        fig, ax = plt.subplots()
        ax.plot_date(x_axis, y_axis)
        # Major ticks every half year, minor ticks every month,
        ax.xaxis.set_major_locator(mdates.DayLocator())
        #ax.xaxis.set_minor_locator(mdates.MonthLocator())
        ax.grid(True)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
        # Rotates and right-aligns the x labels so they don't crowd each other.
        for label in ax.get_xticklabels(which='major'):
            label.set(rotation=30, horizontalalignment='right')
        plt.show() """

def pd_csv_read():
    dataframe = pd.read_csv("data.csv")
    #dataframe["date"] = pd.to_datetime(dataframe["date"]) 
    dates = dataframe["date"]
    surge_count = dataframe["surge_count"]
    print(dates[1])    

csv_read()

t = t[1:len(t)]

fig, ax = plt.subplots()
ax.plot_date(t, surge_count)
#ax.xaxis.set_major_locator(mdates.DayLocator(2))
ax.xaxis.set_minor_locator(mdates.DayLocator(4))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

ax.grid(True)
plt.show()        


#pd_csv_read()
#csv_read()
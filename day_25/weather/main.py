# with open("weather_data.csv") as weather_file:
#     weather = weather_file.readlines()
#     print(weather)

import csv

import pandas
import math
import pandas as pd
from numpy.ma.extras import average

with open("weather_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    temperatures = []
    for row in reader:
        if row[1] != "temp":
          temperatures.append(int(row[1]))
    print(temperatures)
data = pandas.read_csv("weather_data.csv")
temp = data[data["day"]=="Monday"]
monday_tem = temp["temp"][0]
print(monday_tem)
tem_ferheniet = int(monday_tem)*9/5 + 32
print(tem_ferheniet)
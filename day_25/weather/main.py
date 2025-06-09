# with open("weather_data.csv") as weather_file:
#     weather = weather_file.readlines()
#     print(weather)

import csv
import pandas as pd

with open("weather_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    temperatures = []
    for row in reader:
        if row[1] != "temp":
          temperatures.append((row[1]))
    print(temperatures)

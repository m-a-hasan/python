# # with open("weather_data.csv") as weather:
# #     data = weather.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as weather:
# #     data = csv.reader(weather)
# #     next(data)
# #     temperatures = []
# #     # print(data)
# #     for row in data:
# #         # print(row)
# #         temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# print("Full data")
# print(data)
# print("Just the temperature")
# print(data["temp"])
# print(f"Pandas data type: {type(data)}")
# print(f"Pandas column data type: {type(data['temp'])}")
# print(f"Average temperature: {data['temp'].mean()}")
# print(f"Maximum temperature: {data['temp'].max()}")
# print(f"Row with the highest temperature of the week: {data[data.temp == data.temp.max()]}")
# monday_temp = data.temp[data.day == 'Monday']
# print(f"Monday's temperature in fahrenheit: {(monday_temp * (9/5)) + 32}")

import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(f"{type(squirrel_data)}")
grey_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# print(gray_fur)
d = {'Fur Color': ["grey", "red", "black"], 'Count': [grey_fur, red_fur, black_fur]}
df = pd.DataFrame(data=d)
df.to_csv("squirrel_count.csv")

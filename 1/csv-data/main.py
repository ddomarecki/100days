# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)

data["temp"].mean()

data["temp"].max()

data.condition

data[data.day == "Monday"]

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday.condition

monday.temp = monday.temp[0]



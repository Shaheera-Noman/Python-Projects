# with open("25.ReadingCSV\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("25.ReadingCSV\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "Temp":
#             temperatures.append(row[1])
#     print(temperatures)

# import pandas
# data = pandas.read_csv("25.ReadingCSV\weather_data.csv")

# print(data)
# print(type(data))
# print(type(data["Temp"]))
# print(data["Temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["Temp"].to_list()
# print(temp_list)

   # AVERAGE OF TEMPERATURE.

# average = sum(temp_list)/len(temp_list)
# print(average)

# print(data["Temp"].mean())
# print(data["Temp"].max())

#    # GET DATA IN COLUMNS.
# print(data["Condition"])
# print(data.Condition)

#    # GET DATA IN ROWS.
# print(data[data.Day == "Monday"])
# print(data[data.Temp == data.Temp.max()])

# monday = data[data.Day == "Monday"]
# # print(monday.Condition)
# monday_temp = int(monday.Temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch.
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("25.ReadingCSV\\new_data.csv")

import pandas

data = pandas.read_csv("25.ReadingCSV\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231030.csv")
# gray_squirrels = data[data["Primary Fur Color"] == "Grey"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels)
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black",],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("25.ReadingCSV\\squirrel_count.csv")
from data import stock
import csv
from datetime import date
from scipy import stats
import os

isolated_column = input("What do you want to predict? (Open/High/Low/Close/Adj Close/Volume) ")

x = []
y = []

today_column = float()

with open(f"{stock}.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        x.append(float(row[isolated_column]))
        y.append(line_count)
        line_count += 1
        if line_count == 5:
            today_column = float(row[isolated_column])

os.remove(f"{stock}.csv")

slope, intercept, r, p, std_err = stats.linregress(x, y)

def model(x):
  return slope * x + intercept

wanted_prediction = int(input("How far ahead from today do you want to predict? ")) + line_count

prediction = model(wanted_prediction)

if today_column < prediction:
    print("The prediction is it will be higher (According to the week).")
elif today_column > prediction:
    print("The prediction is it will be lower (According to the week).")
else:
    print("The prediction is it will stay the same (According to the week).")

print("And the R is:", r)
import csv

fileName='input.csv'
with open(fileName, mode ='r')as file:
    data=[]
    csvFile = csv.reader(file)
    for lines in csvFile:
        data.append(lines)
    data.pop(0)

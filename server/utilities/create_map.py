""" This file is used to create the mapping of unique values from specified rows """

import csv

unique_mapping = {}

with open('zomato_cuisines.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the first line
    next(csv_reader)
    for row in csv_reader:
        unique_mapping[row[1].lower()] = "cuisine"

with open('zomato.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        unique_mapping[row[3].lower()] = "city"

with open('country_code.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        unique_mapping[row[1].lower()] = "country_name"


with open('zomato.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        unique_mapping[row[18].lower()] = "rating_text"

with open('zomato.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        unique_mapping[row[10].lower()] = "currency"

print(unique_mapping)

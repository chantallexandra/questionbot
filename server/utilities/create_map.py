""" This file is used to create the mapping of unique values from specified rows"""

import csv

# unique_cuisines = set()
# unique_cities = set()
# unique_countries = set()
# unique_rating = set()
# unique_currencies = set()
#
# with open('zomato_cuisines.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     # skip the first line
#     next(csv_reader)
#     for row in csv_reader:
#         unique_cuisines.add(row[1])
#     print(unique_cuisines)
#
# with open('zomato.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         unique_cities.add(row[3])
#     print(unique_cities)
#
# with open('country_code.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         unique_countries.add(row[1])
#     print(unique_countries)
#
#
# with open('zomato.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         unique_rating.add(row[18])
#     print(unique_rating)
#
# with open('zomato.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         unique_currencies.add(row[10])
#     print(unique_currencies)

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

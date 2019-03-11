"""
    This file was used to create a csv (now called zomato_cuisines of cuisines
    for each restaurant from the original file which had cuisines comma separated
    in a single string
"""
import csv

output_file = open('zomato_cuisines_edited.csv', mode='w')
output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

with open('zomato_cuisines.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cuisine_types = row[1].split(", ")
        for type in cuisine_types:
            output_writer.writerow([row[0], type])
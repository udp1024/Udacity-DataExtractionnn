import os
import csv
import json

rowcounter = 0
clean_data = []

csv_filename = "beatles-diskography.csv"
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        keyslist = row.keys()
        if rowcounter < 3:
            cleanString = "{"
            for key in keyslist:
                cleanString = cleanString + '\"' + key + '\"' + ': ' + '\"' + row[key].strip() + '\"' + ','
            cleanString = cleanString[:-1] + '}'
            print('cleanstring: ', cleanString)
            print('row: ', row)
            print('===')
            clean_data.append(json.loads(cleanString))
            rowcounter += 1
        else:
            break
    data = clean_data
#print('++++')
print(data[0])
print('++++')






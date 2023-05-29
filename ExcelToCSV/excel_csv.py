# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
import numpy

from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = None
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    data = []
    maxCols = sheet.ncols -1

    for col in range(1,maxCols):
        stnName = sheet.cell_value(0, col)
        # get all the col values to calculate the average
        colValues=sheet.col_values(col,start_rowx=1) # skipping the header row
        maxCOAST = numpy.amax(colValues)
        maxIndex = numpy.argmax(colValues)+1 # adjust for the skipped header row
        maxDate = xlrd.xldate_as_tuple(sheet.cell_value(maxIndex, 0), 0)
        # avgCOAST = numpy.average(colValues)
        # minCOAST = numpy.amin(colValues)
        # minIndex = numpy.argmin(colValues)+1 
        # minDate = xlrd.xldate_as_tuple(sheet.cell_value(minIndex, 0), 0)
        outDict = {"Station": stnName,"Year":maxDate[0],"Month":maxDate[1],"Day": maxDate[2],"Hour": maxDate[3],"Max Load": maxCOAST}
        data.append(outDict)
    return data

def save_file(data, filename):
    # YOUR CODE HERE
    keys = data[0].keys()
    with open(filename, 'w', encoding='utf8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter='|')
        dict_writer.writeheader()
        dict_writer.writerows(data)
        output_file.close()
    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()

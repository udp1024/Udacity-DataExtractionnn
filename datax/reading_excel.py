#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format

"""

import numpy
import xlrd
from zipfile import ZipFile

zipfile = "2013_ERCOT_Hourly_Load_Data"
excelfile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    # find and return the min, max and average values for the COAST region
    col=1
    maxCOAST = max(sheet.col_values(col, start_rowx=1, end_rowx=sheet.nrows))

    for row in range(sheet.nrows):
        if sheet.cell_value(row, col) == maxCOAST:
            exceltime = sheet.cell_value(row,0)
            maxDate = xlrd.xldate_as_tuple(exceltime, 0)
            break
    
    minCOAST = min(sheet.col_values(col, start_rowx=1, end_rowx=sheet.nrows))
    for row in range(sheet.nrows):
        if sheet.cell_value(row, col) == minCOAST:
            exceltime = sheet.cell_value(row,0)
            minDate = xlrd.xldate_as_tuple(exceltime, 0)
            break
    
    # get all the COAST col values to calculate the average
    colValues=sheet.col_values(1,start_rowx=1)
    avgCOAST = numpy.average(colValues)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }

    data.update({"maxtime": maxDate, "maxvalue": maxCOAST, "mintime": minDate, "minvalue": minCOAST, "avgcoast": avgCOAST,})


    return data


def test():
    open_zip(zipfile)
    data = parse_file(excelfile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()

# this file sets up the CLI in Python for interactive coding for excel_csv.py app
# python3
# exec(open("ExcelToCSV/cli_setup.py").read())

import xlrd
import numpy
import csv

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

# def parse_file(datafile):
workbook = xlrd.open_workbook(datafile)
sheet = workbook.sheet_by_index(0)

data = None
# YOUR CODE HERE
# Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
# Excel date to Python tuple of (year, month, day, hour, minute, second)
data = []
maxCols = sheet.ncols

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

# we got data (a list of dictionaries) back from the parse function
# lets get the keys
keys = data[0].keys()
with open('excelToCSV.csv', 'w', encoding='utf8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, delimiter='|')
    dict_writer.writeheader()
    dict_writer.writerows(data)
    output_file.close()




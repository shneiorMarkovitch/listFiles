import csv

def writeOnCsv(onlyfiles):
    with open('../csv_files.csv', 'wb') as f:
        csv.excel.delimiter = ';'
        writer = csv.writer(f, dialect=csv.excel)
        writer.writerow([onlyfiles])

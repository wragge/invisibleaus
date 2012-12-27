import csv


def import_nsw_bdm(csv_filepath):
    with open(csv_filepath, 'rb') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            print row[0]


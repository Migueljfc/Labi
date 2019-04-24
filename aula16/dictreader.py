import csv
import sys
def main(argv):
    fich_csv = open(argv[1], "r")
    csv_dictreader = csv.DictReader(fich_csv, delimiter=',')
    for row in csv_dictreader:
        print(row)
main(sys.argv)
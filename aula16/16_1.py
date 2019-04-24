import csv;
import sys;

def main(argv):
    soma=0
    cont=0
    tempMax=-10
    tempMin=10
    fich_csv = open(argv[1], "r")
    csv_reader = csv.reader(fich_csv, delimiter=',')
    for row in csv_reader:
        try:
            temp = float(row[3])
        except:
            continue

        soma = soma + temp
        cont+=1
        if temp>tempMax:
            tempMax=temp
        if temp<tempMin:
            tempMin=temp
    media = soma/cont
    print("tempertatura minima : %.2f" %tempMax)
    print("temperatura maxima : %.2f" %tempMin)
    print("media de temperaturas : %.2f" %media)



main(sys.argv)

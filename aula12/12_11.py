import sys
ano = int(sys.argv[1])
if (ano%4==0 and ano%100!=0)or ano%400==0:
    bissexto = True
else:
    bissexto = False
print (bissexto)
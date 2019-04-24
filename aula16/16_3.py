import csv
import psutil
import time
def main ():
    fout = open("regist.csv", "w")
    writer  = csv.DictWriter(fout,fieldnames=['time','cpu','send','recv'],delimiter = ';')
    writer.writeheader()
    t0=time.time()
    tm=t0
    while tm-t0<10:
        cpu = psutil.cpu_percent(interval=1)
        print(cpu)
        tm=time.time()
        net = psutil.net_io_counters()
        print(net)
        data = {'time':tm, 'cpu' : cpu, 'send':net[0], 'recv':net[1]}
        writer.writerow(data)
    
    fout.close()
main()
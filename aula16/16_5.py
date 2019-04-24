import csv
import psutil
import time
import json
def main ():
    fout = open("regist.json", "w")
    d = {'stats':[0]}
    t0=time.time()
    tm=t0
    while tm-t0<10:
        cpu = psutil.cpu_percent(interval=1)
        print(cpu)
        tm=time.time()
        net = psutil.net_io_counters()
        print(net)
        data = {'time':tm, 'cpu' : cpu, 'send':net[0], 'recv':net[1]}
        d['stats'].append(data)
    fout.write(json.dumps(d,indent=4))
    fout.close()
main()
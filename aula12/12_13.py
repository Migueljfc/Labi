import sys 
n = int(sys.argv[1])
l=[1,1]
for i in range(2,n):
    x = l[i-1]+l[i-2]
    l.append(x)
print(l)
import sys
def fibonacci(n):
    fb = []
    if n < 1:
        fb = []
    if n == 1:
        fb = [0,1]
    if n == 2:
        fb = [0,1,1]
    if n > 2:
        fb = [0,1,1]
        for i in range(3,n+1):
            x = fb[i-2]+fb[i-1]
            fb.append(x)
    
    return fb
##################################################
def usage(progname):
    print("Usage: python3 %s number"%(progname))
##################################################
def main(argv):
    if(len(argv)!=2):
        usage(argv[0])
        sys.exit(1)
    if not argv[1].isdigit():
        usage(argv[0])
        sys.exit(2)
    
    print(fibonacci(int(argv[1])))
    sys.exit(0) #Exit code 0 run OK

main(sys.argv)
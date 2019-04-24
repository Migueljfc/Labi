import sys

def main(argv):
    num = int(argv[1])
    for x in range(2, num//2):
        if num % x == 0:
            print("False") 
            quit()
    print("True")
main(sys.argv)
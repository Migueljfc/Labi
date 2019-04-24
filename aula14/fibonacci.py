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
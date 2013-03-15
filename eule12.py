import math
from functools import reduce

def tnum(n):
    tn = 0
    
    while(n > 0):
        tn += n
        n -= 1
        
    return tn

def div(n):
    r = []
    for d in range(1,int(math.sqrt(n))):
        if(n%d == 0):
            r.append(d)
    
    return r

def primefac(n):
    fl=[]
    x=2
    while(x <= n):
        if(n % x== 0):
            n /= x
            fl.append(x)
        else:
            x += 1
            
    return fl


def istnum(n):
    if(math.floor(math.sqrt(n*8 + 1)) == math.sqrt(n*8 + 1)):
        return True
    
    return False





n = 0
i = 1

while(len(div(n))*2 < 500):
    n += i;
    i += 1
    
print(n)    



    

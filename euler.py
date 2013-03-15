import math 

def prod(lst):
    p = 1
    for n in lst:
        if(p == 0):
            return 0
        
        p = p*int(n)
            
    return p


def ispan(n):
    if(len(list(set(str(n)))) == len(str(n)) == 9) and ('0' not in str(n)):
           return True
       
    return False

def ispan2(n):
    if('0' in str(n)):
        return False
    if(int(len(list(set(str(n))))) == int(len(str(n))) == int(max(list(str(n))))):
        return True
    
    return False


def ispal(n):
    if(str(n) == str(n)[::-1]): 
        return True
    
    return False


def tobin(n):
    return(str(bin(n))[2:len(bin(n))])


def isprime(n):
    if(n < 0 ):
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def divs(n):
    r = []
    for d in range(1, n+1):
        print(d)
        if(n%d == 0):
            r.append(d)
    
    return r


def period(n):
    if(isprime(n)):
        p = 1
        while True:
            if((pow(10,p) - 1) % n == 0):
                return p
            else:
                p += 1
                
    return 0


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


def factors(n):
    lower = [1]
    upper = [n]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):   
            lower.append(i)
            upper.append(int(n/i))
    upper.reverse()
    return lower + upper


units = ["", "one", "two", "three", "four",  "five", 
    "six", "seven", "eight", "nine "]

tex = ["", "eleven", "twelve", "thirteen",  "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "ten", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"]


def w2n(n):
    ns = str(n)
    nl = len(ns)
    nw = ''

    if(nl == 4):
        nw = 'onethousand'
    elif(nl == 3):
        #sute
        nw = units[int(ns[0])] + 'hundred'
        #zeci
         #mizerie
        if(int(ns[1:3]) == 10):
            nw = nw + 'ten'
        elif(int(ns[1:3]) < 10):
            nw = nw + 'and' + units[int(ns[2])] 
        elif((int(ns[1:3]) < 20) and (int(ns[1:3]) > 10)):
#            print(int(ns[1:3]))
#            print(tex[int(ns[1:3][1])])
            nw = nw + 'and' + tex[int(ns[1:3][1])]
        elif(int(ns[1:3]) >= 20):
            nw = nw + 'and' + tens[int(ns[1])]
            #unitati
            nw = nw + units[int(ns[2])]          
      
        nw = nw.replace(" ", "")
    elif(nl == 2):
        #mizerie
        if(n == 10):
            nw = 'ten'
        elif(n < 20):
            nw = tex[int(ns[1])]
        else:
            #zeci
            nw = tens[int(ns[0])]    
            #unitati
            nw = nw + units[int(ns[1])]
#        nw = nw.replace(" ", "")
            
    elif(nl == 1):
        #unitati
        nw = units[int(ns[0])]
    
    nw = nw.replace(" ", "")                
    return nw 

 

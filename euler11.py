import re, linecache

def prod(lst):
    p = 1
    for n in lst:
        if(p == 0):
            return 0
        
        p = p*int(n)
            
    return p 

grid = open('euler11.txt', 'r')


dig = re.compile(r'(\d\d)')

mat = []
for line in grid:
    line = line.split(' ')
    line = list(map(int, line))
    mat.append(line)


rowp = []

for row in mat:
    for s in range(3):
        for i in range(s, len(row), 4):
#            print(row[i:i+4])
            rowp.append(prod(row[i:i+4]))
                      


colp = []

for cnt in range(20):
    c = []
    for col in mat:   
        c.append(col[cnt])
    for s in range(3):
        for i in range(s, len(c), 4):
#            print(c[i:i+4])
            colp.append(prod(c[i:i+4]))       


diags = []

for d in reversed(range(20)):
    r = 19
    c = 19 - d
    ds1 = []
    while(r > -1 and c > -1):
        ds1.append(mat[c][r])
        r -= 1
        c -= 1
    diags.append(ds1)
    
for d in reversed(range(20)):
    r = 19
    c = 19 - d
    ds2 = []
    while(r > -1 and c > -1):
        ds2.append(mat[r][c])
        r -= 1
        c -= 1  
    diags.append(ds2)
        
del diags[-1]

dsp = []
for d in diags:
    for s in range(4):
        for i in range(s, len(d), 4):
#                print(d[i:i+4])
                if(len(d[i:i+4]) == 4):
#                    print(d[i:i+4])
                    dsp.append(prod(d[i:i+4]))  




diagp = []

for d in range(20):
    r = d
    c = 0
    dp1 = []
    while(r > -1 and c < d+1):
#        print(mat[r][c])
        dp1.append(mat[r][c])
        r -= 1
        c += 1
    diagp.append(dp1)
    
for d in range(20):
    r = 19
    c = 19 -d
    dp2 = []
    while(r > -1 and c < 20):
        dp2.append(mat[r][c])
        r -= 1
        c += 1
    diagp.append(dp2)        

del diagp [-1]

dpp = []
for d in diagp:
    for s in range(4):
        for i in range(s, len(d), 4):
#                print(d[i:i+4])
                if(len(d[i:i+4]) == 4):
#                    print(d[i:i+4])
                    dpp.append(prod(d[i:i+4]))  


   

print(max(rowp))
print(max(colp)) 
print(max(dsp))
print(max(dpp))
      
   
        









    


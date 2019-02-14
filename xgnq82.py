import numpy as np
def message(a):
    l = len(a)
    rfound = False
    r=2
    m=[]
    while rfound == False:
        k = 2**r - r - 1
        if k-r >= l :
            rfound = True
        else:
            r+=1
    m.extend(decimalToVector(l,r))
    m.extend(a)
    for i in range (0, k-len(m)):
        m.append(0)
    return m

def hammingEncoder(m):
    r=2
    rfound = False
    while rfound == False:
        k = 2**r - r - 1
        if k > len(m) :
            rfound = True
            return []
        elif k == len(m):
            rfound = True
        else:
            r+=1
    g = hammingGeneratorMatrix(r)
    n = (np.matmul(m,g)%2).tolist()   
    return n

def hammingDecoder(v):
    k = len(v)
    r=2
    rfound = False
    while rfound == False:
        if k == 2**r - 1 :
            rfound = True
        elif k < 2**r - 1:
            return []
        else:
            r+=1
    HT =[]
    for i in range(1, 2**r):
        HT.append(decimalToVector(i,r))
    vHT = (np.matmul(v,HT)%2).tolist()
    j = len(vHT)-1
    i=0
    for num in vHT:
        if num == 1:
            i = i + 2**j
        j=j-1
    if i != 0:        
        if v[i-1] == 1:
            v[i-1] = 0
        else:
            v[i-1] = 1
    return v

def messageFromCodeword(c):
    k = len(c)
    r=2
    rfound = False
    while rfound == False:
        if k == 2**r - 1 :
            rfound = True
        elif k < 2**r - 1:
            return []
        else:
            r+=1
    m = []
    positions = []
    for i in range(0,r):
        positions.append(2**i-1)
    j=0
    for i in range(0,len(c)):
        if i not in positions:
            m.append(c[i])
    return m

def dataFromMessage(m):
    k = len(m)
    r=2
    rfound = False
    while rfound == False:
        if k == 2**r - r - 1 :
            rfound = True
        elif k < 2**r - r - 1:
            return []
        else:
            r+=1
    b=1
    l=0
    for i in range (r-1,-1,-1):
        if m[i] == 1:
            l+=b
        b*=2
    v=[]
    if l > len(m)-r:
        return[]
    else :
        for i in range (r,r+l):
            v.append(m[i])
    return v

def repetitionEncoder(m,n):
    c = []
    for i in range(0,n):
        c.append(m[0])
    return c

def repetitionDecoder(v):
    one = 0
    zero = 0
    for i in v:
        if i==1:
            one+=1
        else:
            zero+=1
    if one > zero:
        m = [1]
    elif zero > one:
        m = [0]
    else:
        m = []
    return m

#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G


#function decimalToVector
#input: numbers n and r (0 <= n<2**r)
#output: a string v of r bits representing n
def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

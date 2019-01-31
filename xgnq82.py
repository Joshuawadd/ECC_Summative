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
    return []

def hammingDecoder(v):
    return []

def messageFromCodeword(c):
    return []

def dataFromMessage(m):
    return []

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

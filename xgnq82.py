def message(a):
    return []

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

def GCD(a, b):
    if b == 0: 
        return a
    return GCD(b, a % b)

def LCM(a , b):
    x=GCD(a,b)
    return (a*b)/x

print(LCM(15, 20))
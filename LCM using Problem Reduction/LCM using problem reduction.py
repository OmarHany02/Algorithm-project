def GCD(a, b):
    if b == 0: 
        return a
    return GCD(b, a % b)

def LCM(a , b):
    x=GCD(a,b)
    print("The GCD is :" ,x)
    return (a*b)/x

print("and the LCM is :",LCM(15, 20))
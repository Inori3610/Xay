def Fibanocci(n):
    if n <=2:
        return [2]
    F = [2, 3]
    
    while len(F) <= n:
        next_value = F[len(F) - 1] + F[len(F) - 2]
        F.append(next_value)
    return F

print(" sau  so dau tien:")
print( Fibanocci(5))

def fibanocci(n):
    F=[2,3]
    for i in range (2,n):
        F.append(F[-1]+F[-2])
    return F
n=6
F=fibanocci(n)
max1=max(F)
min1=min(F)
result=fibanocci(n)
print(f" fibanocci thu {n} :",result)
print( "fibanocci max :",max1 )
print( "fibanocci min :",min1 )

import marth
def scp()

def fib(n):
    return scp(5*n*n+4)


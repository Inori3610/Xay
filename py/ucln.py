def ucln(a,b):
    if b==0:
        return a
    elif a%b==0 :
        return b
    else:
        return ucln(b, a%b)
a=int(input(" nhap so nguyen thu nhat:")) 
b= int(input(" nhap so nguyen thu hai:"))
print (f" uoc chung lon nhat cua ha so la :",ucln(a,b))
chan=[]
tongsc=0
le=[]
tongsl=0
a=int(input(" Nhap so a :"))
b=int(input(" Nhap so b :"))
for i in range(a,b+1):
    if i%2 ==0 :
        chan.append(i)
        tongsc +=i
    else:
        le.append(i)
        tongsl +=i
print (" Day so chan:",chan)
print (" Tong cac so chan",tongsc)
print (" Day so le:",le)
print ("Tong cac so le",tongsl)
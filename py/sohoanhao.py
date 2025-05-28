n=int(input("Nhap so n:"))
S=0
for i in range(1,n):
    if n%i==0:
        S=S+i
if S==n:
    print(n,"La so hoan hao")
else:
    print(n,"Khong phai lam so hoan hao")
    
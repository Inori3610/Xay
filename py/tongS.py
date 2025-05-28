n=list(map(int,input("Nhap day so: ").split()))
s=int(input("Nhap so s :"))
ds=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==s:
            ds.append((n[i],n[j]))
if ds:
    print(f"cac cap (a+b)={s} la:")
    for a,b in ds:
        print(f"({a},{b})")
else:
    print("Khong co cap nao thoan man")
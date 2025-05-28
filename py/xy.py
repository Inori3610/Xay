x=int(input("nhap so nguyen x:"))
y=int(input("nhap so nguyen y:"))
tong=0
for i in range(x,y+1):
    tong +=i**2
print("tong binh phuong x den y:",tong)
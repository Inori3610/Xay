from collections  import deque
queue= deque()
queue.append("A")
queue.append("B")
queue.append("C")
queue.appendleft("D")
print(queue)
first=queue.popleft()
print(first)
print(queue)

from collections import deque
queue=deque([
    ("phuong",2000),
    ("Quynh",500),
    (" Nga",1000),
 ])
queue.appendleft(("xay",3000))
bank_balance =3000
print(" bat dau xu ly giao dich:")
while queue:
    customer, amount= queue.popleft()
    if bank_balance >=amount:
        bank_balance -= amount
        print(f"{customer} daa rut {amount}$. so du con lai:{bank_balance}$:")
    elif bank_balance<0 :
        queue.appendleft()
        bank_balance += customer
        print(f" khach hang gui tien :")
        
    else:
        print(f" ngan hang khong du tien de phuc vu {customer} ({amount}$):")
print(" KET THUC GIAO DICH")


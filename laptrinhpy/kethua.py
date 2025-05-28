import pickle

class Qlbanhang:
    def __init__(self):
        self.makhachhang = ""
        self.tenkhachhang = ""
        self.diachi = ""
        self.sdt = ""
        self.SoluongSPmua = 0
        self.Dongia = 0.0

    def nhap(self):
        self.makhachhang = input("Nhập mã khách hàng: ")
        self.tenkhachhang = input("Nhập tên khách hàng: ")
        self.diachi = input("Nhập địa chỉ: ") 
        self.sdt = input("Nhập số điện thoại: ")
        self.SoluongSPmua = int(input("Nhập số lượng sản phẩm mua: "))
        self.Dongia = float(input("Nhập đơn giá: "))

    def xuat(self):
        print(f"Mã KH: {self.makhachhang}")
        print(f"Tên KH: {self.tenkhachhang}")
        print(f"Địa chỉ: {self.diachi}")
        print(f"SĐT: {self.sdt}")
        print(f"Số lượng SP mua: {self.SoluongSPmua}")
        print(f"Đơn giá: {self.Dongia}")

class vidbanhang(Qlbanhang):
    def __init__(self):
        super().__init__()
        self.chietkhau = 0.0

    def nhap(self):
        super().nhap()
        self.chietkhau = float(input("Nhập chiết khấu (%): "))

    def xuat(self):
        super().xuat()
        print(f"Chiết khấu: {self.chietkhau}%")
        print(f"Tổng tiền: {self.tongtien():,.2f} đ")

    def tongtien(self):
        muahang = self.SoluongSPmua * self.Dongia
        return muahang * (1 - self.chietkhau / 100)

def ghi(filename, dskh):
    with open(filename, "wb") as f:
        pickle.dump(dskh, f)

def doc(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

def main():
    ds = []
    tongdoanhthu = 0
    print("=" * 40)
    n = int(input("Nhập số khách hàng VIP: "))
    for i in range(n):
        print("-" * 30)
        print(f"Nhập khách hàng thứ {i+1}:")
        kh = vidbanhang()
        kh.nhap()
        ds.append(kh)

    # Ghi danh sách vào file
    ghi("D:\\ds.dat", ds)

    print("=" * 40)
    print("Danh sách khách hàng được ghi vào file:")
    print("-" * 20)

    # Đọc file và in danh sách khách hàng
    dskh = doc("D:\\ds.dat")
    for kh in dskh:
        kh.xuat()
        print("-" * 20)
        tongdoanhthu += kh.tongtien()

    print(f"Tổng doanh thu: {tongdoanhthu:,.2f} đ")
    print("=" * 40)

if __name__ == "__main__":
    main()

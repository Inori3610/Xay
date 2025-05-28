# Lớp cha
class Phong:
    def __init__(self, ten_phong, gia_phong):
        self.ten_phong = ten_phong
        self.gia_phong = gia_phong

    def tinh_tien(self, so_ngay):
        return self.gia_phong * so_ngay

    def __str__(self):
        return f"Tên phòng: {self.ten_phong}, Giá phòng: {self.gia_phong} VND/ngày"


# Lớp con
class ThuePhong(Phong):
    def __init__(self, ten_phong, gia_phong, ten_khach_hang, loai_phong):
        super().__init__(ten_phong, gia_phong)
        self.ten_khach_hang = ten_khach_hang
        self.loai_phong = loai_phong.lower()

    def tinh_tien(self, so_ngay):
        tien = super().tinh_tien(so_ngay)
        if self.loai_phong == "vip":
            return tien * 1.1
        return tien

    def __str__(self):
        return (f"Khách hàng: {self.ten_khach_hang}, "
                f"Phòng: {self.ten_phong} ({self.loai_phong.upper()}), "
                f"Giá: {self.gia_phong} VND/ngày")
        
#  menu
def nhap_danh_sach_khach(ds_khach):
    n = int(input("Nhập số lượng khách thuê phòng: "))
    for i in range(n):
        print(f"\nNhập thông tin khách hàng thứ {i+1}:")
        them_khach(ds_khach)

def them_khach(ds_khach):
    ten_khach = input("Tên khách hàng: ")
    ten_phong = input("Tên phòng: ")
    gia_phong = int(input("Giá phòng: "))
    loai_phong = input("Loại phòng (thường/vip): ")
    khach = ThuePhong(ten_phong, gia_phong, ten_khach, loai_phong)
    ds_khach.append(khach)
    print(" Đã thêm khách thành công!")

def sua_thong_tin(ds_khach):
    ten_can_sua = input("Nhập tên khách hàng cần sửa: ")
    for khach in ds_khach:
        if khach.ten_khach_hang.lower() == ten_can_sua.lower():
            print(" Nhập thông tin mới:")
            khach.ten_khach = input("Tên khách hàng mới: ")
            khach.ten_phong = input("Tên phòng mới: ")
            khach.gia_phong = int(input("Giá phòng mới: "))
            khach.loai_phong = input("Loại phòng (thường/vip): ").lower()
            print(" Đã cập nhật thông tin khách!")
            return
    print("Không tìm thấy khách hàng!")

def xoa_khach(ds_khach):
    ten_can_xoa = input("Nhập tên khách hàng cần xóa: ")
    for khach in ds_khach:
        if khach.ten_khach_hang.lower() == ten_can_xoa.lower():
            ds_khach.remove(khach)
            print(" Đã xóa khách hàng!")
            return
    print(" Không tìm thấy khách hàng!")

def hien_thi_danh_sach(ds_khach):
    if not ds_khach:
        print(" Danh sách rỗng!")
        return
    print("\n DANH SÁCH KHÁCH THUÊ PHÒNG:")
    for khach in ds_khach:
        print(khach)
#chinhmenu
def main():
    ds_khach = []
    while True:
        print("\n====== MENU QUẢN LÝ THUÊ PHÒNG ======")
        print("1. Nhập số lượng khách thuê phòng")
        print("2. Thêm một khách thuê phòng mới")
        print("3. Sửa thông tin của khách")
        print("4. Xóa 1 khách hàng theo tên")
        print("5. Thoát")
        print("=====================================")
        chon = input(">> Chọn chức năng (1-5): ")

        if chon == "1":
            nhap_danh_sach_khach(ds_khach)
            hien_thi_danh_sach(ds_khach)
        elif chon == "2":
            them_khach(ds_khach)
            hien_thi_danh_sach(ds_khach)
        elif chon == "3":
            sua_thong_tin(ds_khach)
            hien_thi_danh_sach(ds_khach)
        elif chon == "4":
            xoa_khach(ds_khach)
            hien_thi_danh_sach(ds_khach)
        elif chon == "5":
            print(" Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print(" Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")

print (main())

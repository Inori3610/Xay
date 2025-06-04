<!-- CustomerRegister.php -->
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đăng ký khách hàng</title>
    <style>
        body { font-family: Arial; margin: 40px; background-color: #f9f9f9; }
        form { width: 500px; margin: auto; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        input, select, textarea { width: 100%; padding: 8px; margin: 8px 0; border-radius: 5px; border: 1px solid #ccc; }
        label { font-weight: bold; }
        .buttons { display: flex; justify-content: space-between; }
        .buttons input { width: 48%; }
    </style>
</head>
<body>

<h2 style="text-align:center;">Form Đăng Ký Khách Hàng</h2>

<form action="CustomerRegister.php" method="post">
    <label>Họ và Tên *</label>
    <input type="text" name="fullname" required>

    <label>Email *</label>
    <input type="email" name="email" required>

    <label>Số điện thoại *</label>
    <input type="text" name="phone" required>

    <label>Ngày sinh *</label>
    <input type="date" name="dob" required>

    <label>Địa chỉ</label>
    <textarea name="address" rows="3"></textarea>

    <label>Giới tính *</label><br>
    <input type="radio" name="gender" value="Nam" required> Nam
    <input type="radio" name="gender" value="Nữ" required> Nữ
    <input type="radio" name="gender" value="Khác" required> Khác
    <br><br>

    <label>Loại khách hàng *</label>
    <select name="type" required>
        <option value="">--Chọn loại--</option>
        <option value="Thường">Thường</option>
        <option value="VIP">VIP</option>
        <option value="Doanh nghiệp">Doanh nghiệp</option>
    </select>

    <div class="buttons">
        <input type="submit" name="submit" value="Đăng ký">
        <input type="reset" value="Xóa Form">
    </div>
</form>

</body>
</html>

<?php
// Kết nối CSDL
$conn = new mysqli("localhost", "root", "", "customer_db");
if ($conn->connect_error) die("Kết nối thất bại: " . $conn->connect_error);

// Xử lý khi nhấn Đăng ký
if (isset($_POST['submit'])) {
    $fullname = $_POST['fullname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $dob = $_POST['dob'];
    $address = $_POST['address'];
    $gender = $_POST['gender'];
    $type = $_POST['type'];

    // Chuẩn bị câu lệnh SQL an toàn
    $stmt = $conn->prepare("INSERT INTO customers (fullname, email, phone, dob, address, gender, type) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("sssssss", $fullname, $email, $phone, $dob, $address, $gender, $type);

    if ($stmt->execute()) {
        header("Location: CustomerList.php");
        exit;
    } else {
    echo "<p style='color:red;'>Đăng ký thất bại: " . $stmt->error . "</p>";
    }

    $stmt->close();
}
$conn->close();
?>

<?php
$conn = new mysqli("localhost", "root", "", "customer_db");
if ($conn->connect_error) die("Kết nối thất bại");

if (!isset($_GET['id'])) {
    die("Lỗi: Không tìm thấy ID khách hàng.");
}
$id = $_GET['id'];
$result = $conn->query("SELECT * FROM customers WHERE id=$id");
$row = $result->fetch_assoc();

if (isset($_POST['update'])) {
    $fullname = $_POST['fullname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $dob = $_POST['dob'];
    $address = $_POST['address'];
    $gender = $_POST['gender'];
    $type = $_POST['type'];

    $stmt = $conn->prepare("UPDATE customers SET fullname=?, email=?, phone=?, dob=?, address=?, gender=?, type=? WHERE id=?");
    $stmt->bind_param("sssssssi", $fullname, $email, $phone, $dob, $address, $gender, $type, $id);

    if ($stmt->execute()) {
        echo "<script>alert('Cập nhật thành công!'); window.location='CustomerList.php';</script>";
    } else {
        echo "<script>alert('Lỗi: {$stmt->error}');</script>";
    }
    $stmt->close();
}
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Cập nhật khách hàng</title>
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

<h2 style="text-align:center;">Cập nhật thông tin khách hàng</h2>

<form method="post">
    <label>Họ và Tên *</label>
    <input type="text" name="fullname" value="<?= htmlspecialchars($row['fullname']) ?>" required>

    <label>Email *</label>
    <input type="email" name="email" value="<?= htmlspecialchars($row['email']) ?>" required>

    <label>Số điện thoại *</label>
    <input type="text" name="phone" value="<?= htmlspecialchars($row['phone']) ?>" required>

    <label>Ngày sinh *</label>
    <input type="date" name="dob" value="<?= $row['dob'] ?>" required>

    <label>Địa chỉ</label>
    <textarea name="address" rows="3"><?= htmlspecialchars($row['address']) ?></textarea>

    <label>Giới tính *</label><br>
    <input type="radio" name="gender" value="Nam" <?= ($row['gender'] == 'Nam') ? 'checked' : '' ?>> Nam
    <input type="radio" name="gender" value="Nữ" <?= ($row['gender'] == 'Nữ') ? 'checked' : '' ?>> Nữ
    <input type="radio" name="gender" value="Khác" <?= ($row['gender'] == 'Khác') ? 'checked' : '' ?>> Khác
    <br><br>

    <label>Loại khách hàng *</label>
    <select name="type" required>
        <option value="Thường" <?= ($row['type'] == 'Thường') ? 'selected' : '' ?>>Thường</option>
        <option value="VIP" <?= ($row['type'] == 'VIP') ? 'selected' : '' ?>>VIP</option>
        <option value="Doanh nghiệp" <?= ($row['type'] == 'Doanh nghiệp') ? 'selected' : '' ?>>Doanh nghiệp</option>
    </select>

    <div class="buttons">
        <input type="submit" name="update" value="Cập nhật">
        <input type="reset" value="Xóa Form">
    </div>
</form>

</body>
</html>



<!-- Form tương tự CustomerRegister.php, nhưng có sẵn dữ liệu -->

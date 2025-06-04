<?php
$conn = new mysqli("localhost", "root", "", "customer_db");
if ($conn->connect_error) die("Kết nối thất bại");

$search = "";
if (isset($_GET['search']) && !empty(trim($_GET['search']))) {
    $search = trim($_GET['search']);
    $stmt = $conn->prepare("SELECT * FROM customers WHERE fullname LIKE CONCAT('%', ?, '%') OR email LIKE CONCAT('%', ?, '%') OR type LIKE CONCAT('%', ?, '%')");
    $stmt->bind_param("sss", $search, $search, $search);
    $stmt->execute();
    $result = $stmt->get_result();
} else {
    $result = $conn->query("SELECT * FROM customers");
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Danh sách khách hàng</title>
    <style>
        table { width: 90%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
        th { background-color: #f0f0f0; }
        a { margin: 0 5px; text-decoration: none; }
        form { text-align: center; margin-bottom: 20px; }
    </style>
</head>
<body>

<form method="get" action="CustomerList.php">
    <input type="text" name="search" placeholder="Tìm theo tên, email hoặc loại khách" value="<?= htmlspecialchars($search) ?>">
    <input type="submit" value="Tìm kiếm">
    <a href="CustomerList.php"><button type="button">Tải lại</button></a>
</form>

<h2 style="text-align:center;">Danh sách khách hàng</h2>

<table>
    <tr>
        <th>STT</th>
        <th>Họ và Tên</th>
        <th>Email</th>
        <th>Điện thoại</th>
        <th>Ngày sinh</th>
        <th>Địa chỉ</th>
        <th>Giới tính</th>
        <th>Loại</th>
        <th>Hành động</th>
    </tr>
    <?php
    $i = 1;
    while ($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>{$i}</td>
                <td>{$row['fullname']}</td>
                <td>{$row['email']}</td>
                <td>{$row['phone']}</td>
                <td>{$row['dob']}</td>
                <td>{$row['address']}</td>
                <td>{$row['gender']}</td>
                <td>{$row['type']}</td>
                <td>
                    <a href='UpdateCustomer.php?id={$row['id']}'>Sửa</a> |
                    <a href='DeleteCustomer.php?id={$row['id']}' onclick=\"return confirm('Bạn có chắc muốn xóa?');\">Xóa</a>
                </td>
              </tr>";
        $i++;
    }
    ?>
</table>

<div style="text-align: center; margin-top: 20px;">
    <a href="CustomerRegister.php"><button type="button">← Quay lại trang đăng ký</button></a>
</div>

</body>
</html>

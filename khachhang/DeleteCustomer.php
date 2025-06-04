<?php
$conn = new mysqli("localhost", "root", "", "customer_db");
if ($conn->connect_error) die("Kết nối thất bại");

$id = $_GET['id'];
$conn->query("DELETE FROM customers WHERE id=$id");
echo "Xóa thành công!";
header("Location: CustomerList.php")
?>
include "connect.php";
if (!isset($_GET['id'])) {
    die("Lỗi: Không có ID được truyền.");
}
$id = (int)$_GET['id'];
$sql = "DELETE FROM hocsinh WHERE id = $id";
if ($conn->query($sql) === TRUE) {
    echo "Xóa thành công!";
    header("Location:student.php");
    exit;
} else {
    echo "Lỗi khi xóa: " . $conn->error;
}

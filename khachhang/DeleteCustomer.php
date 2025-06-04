<?php
$conn = new mysqli("localhost", "root", "", "customer_db");
if ($conn->connect_error) die("Kết nối thất bại");

$id = $_GET['id'];
$conn->query("DELETE FROM customers WHERE id=$id");
echo "Xóa thành công!";
header("Location: CustomerList.php")
?>
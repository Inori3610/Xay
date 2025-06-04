<?php
$host = "localhost";
$user = "root";
$password = "";
$dbname = "customer_management";

// 1. Kết nối cơ sở dữ liệu
$conn = new mysqli($host, $user, $password, $dbname);
if ($conn->connect_error) {
    die("Kết nối thất bại: " . $conn->connect_error);
}

// 2. Thêm khách hàng (ví dụ)
function addCustomer($conn, $full_name, $email, $phone, $status) {
    $stmt = $conn->prepare("INSERT INTO customers (full_name, email, phone, status) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $full_name, $email, $phone, $status);

    if ($stmt->execute()) {
        echo "<p>✅ Thêm khách hàng thành công.</p>";
    } else {
        echo "<p>❌ Thêm thất bại: " . $stmt->error . "</p>";
    }

    $stmt->close();
}

// 3. Hiển thị khách hàng theo trạng thái
function displayCustomersByStatus($conn, $status) {
    $stmt = $conn->prepare("SELECT * FROM customers WHERE status = ?");
    $stmt->bind_param("s", $status);
    $stmt->execute();
    $result = $stmt->get_result();

    echo "<h3>Danh sách khách hàng trạng thái: $status</h3>";
    echo "<table border='1' cellpadding='5'><tr>
            <th>ID</th><th>Họ tên</th><th>Email</th><th>Phone</th><th>Trạng thái</th></tr>";
    while ($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>{$row['customer_id']}</td>
                <td>{$row['full_name']}</td>
                <td>{$row['email']}</td>
                <td>{$row['phone']}</td>
                <td>{$row['status']}</td>
              </tr>";
    }
    echo "</table>";

    $stmt->close();
}

// 4. Cập nhật số điện thoại theo trạng thái
function updatePhoneByStatus($conn, $newPhone, $status) {
    $stmt = $conn->prepare("UPDATE customers SET phone = ? WHERE status = ?");
    $stmt->bind_param("ss", $newPhone, $status);

    if ($stmt->execute()) {
        echo "<p>✅ Cập nhật số điện thoại cho trạng thái '$status' thành công.</p>";
    } else {
        echo "<p>❌ Lỗi cập nhật: " . $stmt->error . "</p>";
    }

    $stmt->close();
}

// 5. Xóa khách hàng theo tên miền email
function deleteByEmailDomain($conn, $domain) {
    $likeDomain = "%@" . $domain;
    $stmt = $conn->prepare("DELETE FROM customers WHERE email LIKE ?");
    $stmt->bind_param("s", $likeDomain);

    if ($stmt->execute()) {
        echo "<p>🗑️ Đã xóa tất cả khách hàng có email thuộc miền @$domain.</p>";
    } else {
        echo "<p>❌ Lỗi xóa: " . $stmt->error . "</p>";
    }

    $stmt->close();
}

//// ==========================
// Ví dụ sử dụng các chức năng:
// (Bỏ comment dòng nào bạn muốn chạy)

//addCustomer($conn, "Nguyễn Văn C", "a@example.com", "0123456789", "Active");
//displayCustomersByStatus($conn, "Active");
//updatePhoneByStatus($conn, "0999999999", "Active");
// deleteByEmailDomain($conn, "example.com");

$conn->close();
?>

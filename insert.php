<?php
include "db.php";

// Get form inputs safely
$name = $_POST['name'];
$father = $_POST['fathername'];
$gender = $_POST['gender'];

// Validate inputs
if (empty($name) || empty($father) || empty($gender)) {
    die("Please fill in all required fields.");
}

// File upload handling
$target_dir = "uploads/";
if (!is_dir($target_dir)) {
    mkdir($target_dir, 0777, true);
}

$image = $_FILES['image'] ?? null;
if ($image && $image['error'] === UPLOAD_ERR_OK) {
    // Validate file type
    $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
    $file_type = mime_content_type($image['tmp_name']);
    if (!in_array($file_type, $allowed_types)) {
        die("Only JPG, PNG, and GIF files are allowed.");
    }

    // Sanitize and rename file
    $image_name = basename($image["name"]);
    $image_ext = pathinfo($image_name, PATHINFO_EXTENSION);
    $safe_name = time() . "" . preg_replace("/[^a-zA-Z0-9\.-]/", "_", $image_name);
    $target_file = $target_dir . $safe_name;

    // Move file and insert into database
    if (move_uploaded_file($image["tmp_name"], $target_file)) {
        // Use prepared statements for security
        $stmt = $conn->prepare("INSERT INTO v (name, fathername, gender,images) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $name, $fathername, $gender, $target_file);

        if ($stmt->execute()) {
            echo "Data saved successfully.";
        } else {
            echo "Database Error: " . $stmt->error;
        }

        $stmt->close();
    } else {
        echo "File upload failed.";
    }
} else {
    echo "No valid image file uploaded.";
}

$conn->close();
?>
<?php
include "db.php";


$sql = "SELECT id, name, fathername, gender, images FROM v";
$result = $conn->query($sql);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Show Records</title>
</head>
<body>

<h2>people Records</h2>

<table border="1" cellspacing="0" cellpadding="8">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Fathername</th>
        <th>Gender</th>
        <th>images</th>
    </tr>
    <?php
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>".$row['id']."</td>";
            echo "<td>".$row['name']."</td>";
            echo "<td>".$row['fathername']."</td>";
            echo "<td>".$row['gender']."</td>";
            
            if (!empty($row['images'])) {
                echo "<td><img src='".$row['images']."' width='80'></td>";
            } else {
                echo "<td>No Image</td>";
            }

            echo "</tr>";   
        }
    } else {
        echo "<tr><td colspan='5'>No records found</td></tr>";
    }
    ?>
</table>

</body>
</html>

<?php
$conn->close();
?>

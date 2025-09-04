<?php

$servername = "localhost";
$username = "root";
$passward = "";
$dbname = "vmart";

$conn = new mysqli($servername, $username, $passward, $dbname);

if ($conn->connect_error){
    die("connection failed : ".$conn->connect_error);
}
?>
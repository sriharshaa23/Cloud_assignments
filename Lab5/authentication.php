<?php
    include('connection.php');
    $username = $_POST['user'];
    $password = $_POST['pass'];

        //to prevent from mysqli injection
        $username = stripcslashes($username);
        $password = stripcslashes($password);
        $username = mysqli_real_escape_string($con, $username);
        $password = mysqli_real_escape_string($con, $password);

        

        $sql = "select *from logins where username = '$username' and passwords = '$password'";
        $result = mysqli_query($con, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
        $count = mysqli_num_rows($result);
         
        
        
        

        if($count == 0 && $password == "seethu123"){
          if($username == "admin"){
            header("Location: feedback.php");
          }
          else{
            header("Location: customer.html");
          }
        }
        else{
            echo "<h1> Login failed. Invalid username or password.</h1>";
        }
?>

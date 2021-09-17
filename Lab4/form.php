?php
        if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['phone']) && isset($_POST['address']) && isset($_POST['message'])) {
            $name = $_POST['name']; 
            $email = $_POST['email'];
            $phone = $_POST['phone'];
            $address = $_POST['address'];
            $message = $_POST['message'];
            $filename = "storage.txt";
            echo "<h1 class=\"section-header\">Message has been sent</h1>";
            $userInfo = array('name'=>$name,'email'=>$email,'phone'=>$phone,'address'=>$address
            'message'=>$message);
            file_put_contents($filename, serialize($userInfo));
        }
        else{
           echo "<h1 class=\"section-header\">Message cannot be sent</h1>";
        }
        ?>
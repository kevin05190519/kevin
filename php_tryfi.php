<?php

echo $_POST['one'];



$json = '{"S": 38, "B": 17, "T": 8, "W": 13, "C": 25, "D": 59}';

$obj = json_decode($json);
print $obj->{'S'}; 


?>
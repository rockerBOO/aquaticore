<?php

$aquaticore = new mysqli('localhost', 'root', '', 'aquaticore');

$mysql = new mysqli('localhost', 'root', '', 'col');

$specialists = $mysql->query('SELECT * FROM `specialists`');

if ($mysql->error)
{
    die ($mysql->error);
}

while ($specialist = $specialists->fetch_object())
{    
    $database_id = 0;
    
    if ($specialist->database_id != false)
    {
        $databases = $mysql->query('SELECT database_name FROM `databases` where record_id = ' . $specialist->database_id);
    
        if ($mysql->error) { die($mysql->error); }
    
        while ($database = $databases->fetch_object())
        {
            $ddds = $aquaticore->query('select id from databases_database where name = "' . $database->database_name . '"');
            
            while ($dd = $ddds->fetch_object())
            {            
                $database_id = $dd->id;
            }
            
            break;
        }
    }
    
    $input = array(
        'name'           => $specialist->specialist_name,
        'database_id'    => $database_id
    );
    
    $aquaticore->query('INSERT INTO specialists_specialist (' . implode(',', array_keys($input)) . ', created) VALUES ("' . implode('","', $input) . '", NOW());');

    
    // $aquaticore->query();
    // if ($aquaticore->error != '')
    // {
    //     echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
    //     continue;
    // }
    // $kingdomId = $aquaticore->insert_id;
}

?>
<?php

$aquaticore = new mysqli('localhost', 'root', '', 'aquaticore');

$mysql = new mysqli('localhost', 'root', '', 'col');

$references = $mysql->query('SELECT * FROM `references`');

if ($mysql->error)
{
    die ($mysql->error);
}

while ($reference = $references->fetch_object())
{    
    $database_id = 0;
    
    if ($reference->database_id != false)
    {
        $databases = $mysql->query('SELECT database_name FROM `databases` where record_id = ' . $reference->database_id);
    
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
        'author'      => $reference->author,
        'year'        => $reference->year,
        'title'       => $reference->title,
        'source'      => $reference->source,
        'database_id' => $database_id
    );
    
    echo 'INSERT INTO references_reference (' . implode(',', array_keys($input)) . ', created) VALUES ("' . implode('","', $input) . '", NOW());'."\n";
    $aquaticore->query( 'INSERT INTO references_reference (' . implode(',', array_keys($input)) . ', created) VALUES ("' . implode('","', $input) . '", NOW());');

    
    // $aquaticore->query();
    // if ($aquaticore->error != '')
    // {
    //     echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
    //     continue;
    // }
    // $kingdomId = $aquaticore->insert_id;
}

?>
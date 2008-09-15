<?php

/*
    Installing index for taxa.Phylum model
    Installing index for taxa.Class model
    Installing index for taxa.Order model
    Installing index for taxa.Family model
    Installing index for taxa.Genus model
    Installing index for taxa.Species model
    Installing index for taxa.Infraspecies model
*/

$aquaticore = new mysqli('localhost', 'root', 'firefly12!', 'aquaticore');

$mysql = new mysqli('localhost', 'root', 'firefly12!', 'CoL2008AC');
if ($kingdom = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Kingdom" AND name = "Animalia"'))
{
    while ($kingdom_row = $kingdom->fetch_object())
    {
        $aquaticore->query('INSERT INTO taxa_kingdom (name, is_accepted_name, created) VALUES ("' .$kingdom_row->name . '", "' . $kingdom_row->is_accepted_name . '", NOW())');
        if ($aquaticore->error != '')
        {
            echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
            continue;
        }
        $kingdomId = $aquaticore->insert_id;
        
        // -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        if ($phylum = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Phylum" AND parent_id = ' . $kingdom_row->record_id . ' GROUP BY name ORDER BY name ASC'))
        {
            while ($phylum_row = $phylum->fetch_object())
            {
                $aquaticore->query('INSERT INTO taxa_phylum (name, is_accepted_name, kingdom_id, created) VALUES ("' .$phylum_row->name . '", "' . $phylum_row->is_accepted_name . '", "' . $kingdomId . '", NOW())');
                if ($aquaticore->error != '')
                {
                    echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                    continue;
                }
                $phylumId = $aquaticore->insert_id;
                
                if ($class = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Class" AND parent_id = ' . $phylum_row->record_id . ' GROUP BY name ORDER BY name ASC'))
                {
                    while ($class_row = $class->fetch_object())
                    {
                        $aquaticore->query('INSERT INTO taxa_class (name, is_accepted_name, phylum_id, created) VALUES ("' .$class_row->name . '", "' . $class_row->is_accepted_name . '", "' . $phylumId . '", NOW())');
                        if ($aquaticore->error != '')
                        {
                            echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                            continue;
                        }
                        
                        $classId = $aquaticore->insert_id;
                        
                        if ($order = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Order" AND parent_id = ' . $class_row->record_id . ' GROUP BY name ORDER BY name ASC'))
                        {
                            while ($order_row = $order->fetch_object())
                            {
                                $aquaticore->query('INSERT INTO taxa_order (name, is_accepted_name, fish_class_id, created) VALUES ("' .$order_row->name . '", "' . $order_row->is_accepted_name . '", "' . $classId . '", NOW())');
                                if ($aquaticore->error != '')
                                {
                                    echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                                    continue;
                                }
                                    
                                $orderId = $aquaticore->insert_id;
                                
                                if ($family = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Family" AND name <> "Not assigned" AND parent_id = ' . $order_row->record_id . ' GROUP BY name ORDER BY name ASC'))
                                {
                                    while ($family_row = $family->fetch_object())
                                    {
                                        $aquaticore->query('INSERT INTO taxa_family (name, is_accepted_name, order_id, created) VALUES ("' .$family_row->name . '", "' . $family_row->is_accepted_name . '", "' . $orderId . '", NOW())');
                                        if ($aquaticore->error != '')
                                        {
                                            echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                                            continue;
                                        }
                                            
                                        $familyId = $aquaticore->insert_id;
                                        
                                        if ($genus = $mysql->query('SELECT name, record_id, is_accepted_name FROM taxa WHERE taxon = "Genus" AND parent_id = ' . $family_row->record_id . ' GROUP BY name ORDER BY name ASC'))
                                        {
                                            while ($genus_row = $genus->fetch_object())
                                            {
                                                $aquaticore->query('INSERT INTO taxa_genus (name, is_accepted_name, family_id, created) VALUES ("' . $genus_row->name . '", "' . $genus_row->is_accepted_name . '", "' . $familyId . '", NOW())');
                                                if ($aquaticore->error != '')
                                                {
                                                    echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                                                    continue;
                                                }
                                                $genusId = $aquaticore->insert_id;
                                                
                                                if ($species = $mysql->query('SELECT name, record_id, is_accepted_name  FROM taxa WHERE taxon = "Species" AND parent_id = ' . $genus_row->record_id . ' GROUP BY name ORDER BY name ASC'))
                                                {
                                                    while ($species_row = $species->fetch_object())
                                                    {
                                                        $aquaticore->query('INSERT INTO taxa_species (name, is_accepted_name, genus_id, created) VALUES ("' . $species_row->name . '", "' . $species_row->is_accepted_name . '", "' . $genusId . '", NOW())');
                                                        if ($aquaticore->error != '')
                                                        {
                                                            echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
                                                            continue;
                                                        }
                                                        $speciesId = $aquaticore->insert_id;
                                                        
                                                        echo $kingdom_row->name . ' ' . $phylum_row->name . ' ' . $class_row->name . ' ' . $order_row->name . ' ' . $family_row->name . ' ' . $genus_row->name . ' ' . $species_row->name . "\n";
                                                        
                                                        
                                                    }
                                                }
                                                else
                                                {
                                                    echo "No species results\n";
                                                }
                                            }
                                        }
                                        else
                                        {
                                            echo "No genus results\n";
                                        }
                                    }
                                }
                                else
                                {
                                    echo "No family results\n";
                                }
                            }
                        }
                        else
                        {
                            echo "No order results\n";
                        }
                    }
                }
                else
                {
                    echo "No class results\n";
                }
            }
        }
        else
        {
            echo "No phylum results\n";
        }
    }
}
else
{
    echo "No kingdom results\n";
}

/*


do 
{
    $result = $mysql->store_result();

    while ($row = $result->fetch_row())
    {
        printf("%s\n", $row[0]);
    }
               
} while($mysql->next_result());


// if ($result = $mysql->use_result())
// {
//     while ($row = $result->fetch_row())
//     {
//         printf("%s\n", $row[0]);
//     }
// }

*/

?>
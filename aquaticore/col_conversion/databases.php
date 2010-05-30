<?php

$aquaticore = new mysqli('localhost', 'root', '', 'aquaticore');

$mysql = new mysqli('localhost', 'root', '', 'col');

$databases = $mysql->query('SELECT * FROM `databases`');

if ($mysql->error)
{
    die ($mysql->error);
}

print_r($databases);

while ($database = $databases->fetch_object())
{
    /*
    database = {
        'display_name' : 'database_name_displayed',
        'database_name' : 'database_name_displayed',
        'database_full_name' : 'database_name_displayed',
        'web_site' : 'web_site',
        'organization' : 'organization',
        'contact_person' : 'contact_person',
        'taxa' : 'taxa',
        'taxonomic_coverage' : 'taxonomic_coverage',
        'abstract' : 'abstract',
        'version' : 'version',
        'release_date' : 'release_date',
        'species_count' : 'SpeciesCount',
        'species_est' : 'SpeciesEst',
        'author_or_editor' : 'author_or_editor',
        'accepted_species_names' : 'accepted_species_names',
        'accepted_infraspecies_names' : 'accepted_infraspecies_names',
        'species_synonyms' : 'species_synonyms',
        'infraspecies_synonyms' : 'infraspecies_synonyms',
        'common_names' : 'common_names',
        'total_names' : 'total_names',
    }
    */
    
        // name                        = models.CharField(max_length=200)
        // full_name                   = models.CharField(max_length=200)
        // display_name                = models.CharField(max_length=200)
        // link                        = models.CharField(max_length=200)
        // contact_person              = models.CharField(max_length=200)
        // taxa                        = models.CharField(max_length=200)
        // taxonomic_converage         = models.CharField(max_length=200)
        // abstract                    = models.CharField(max_length=200)
        // version                     = models.CharField(max_length=200)
        // release_date                = models.CharField(max_length=200)
        // organization                = models.CharField(max_length=200)
        // species_est                 = models.IntegerField(10)
        // authors_editors             = models.CharField(max_length=200)
        // accepted_species_names      = models.IntegerField(10)
        // accepted_infraspecies_names = models.IntegerField(10)
        // species_synonyms            = models.IntegerField(10)
        // infraspecies_synoyms        = models.IntegerField(10)
        // common_names                = models.IntegerField(10)
        // total_names                 = models.IntegerField(10)
        // species_count               = models.IntegerField(10)
        // created                     = models.DateTimeField('date published')
        // modified                    = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
    
    $input = array(
        'display_name'           => $database->database_name_displayed,
        'name'                   => $database->database_name,
        'full_name'              => $database->database_full_name,
        'link'               => $database->web_site,
        'organization'           => $database->organization,
        'contact_person'         => $database->contact_person,
        'taxa'                   => $database->taxa,
        'taxonomic_coverage'     => $database->taxonomic_coverage,
        'abstract'               => $database->abstract,
        'version'                => $database->version,
        'release_date'           => $database->release_date,
        'species_count'          => $database->SpeciesCount,
        'species_est'            => $database->SpeciesEst,
        'authors_editors'     => $database->authors_editors,
        'accepted_species_names' => $database->accepted_species_names,
        'species_synonyms'       => $database->species_synonyms,
        'infraspecies_synonyms'  => $database->infraspecies_synonyms,
        'common_names'           => $database->common_names,
        'total_names'            => $database->total_names
    );
    
    echo 'INSERT INTO databases_database (' . implode(',', array_keys($input)) . ', created) VALUES ("' . implode('","', $input) . '", NOW());'."\n";

    
    // $aquaticore->query();
    // if ($aquaticore->error != '')
    // {
    //     echo __LINE__ . ' ' . $aquaticore->error . ' ' . $aquaticore->insert_id  . "\n";
    //     continue;
    // }
    // $kingdomId = $aquaticore->insert_id;
}

?>
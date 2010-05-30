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

distribution = {
	'code' : 'name_code',
	'location' : 'distribution'
}


# Creating table taxa_kingdom
# Creating table taxa_phylum
# Creating table taxa_class
# Creating table taxa_order
# Creating table taxa_family
# Creating table taxa_genus
# Creating table taxa_species
# Creating table taxa_infraspecies


taxa = {
	'taxa_kingdom' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_phylum' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_class' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_order' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_family' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_genus' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_species' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
	'taxa_infraspecies' : {
		'type'  : taxa:taxan['Kingdom'],
		'title' : taxa:taxon['name_with_italics'],
		'lsid'  : 'taxa:lsid'
	},
}
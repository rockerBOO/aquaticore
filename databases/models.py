from django.db import models

# database = {
#     'display_name' : 'database_name_displayed',
# 	'database_name' : 'database_name_displayed',
# 	'database_full_name' : 'database_name_displayed',
# 	'web_site' : 'web_site',
# 	'organization' : 'organization',
# 	'contact_person' : 'contact_person',
# 	'taxa' : 'taxa',
# 	'taxonomic_coverage' : 'taxonomic_coverage',
# 	'abstract' : 'abstract',
# 	'version' : 'version',
# 	'release_date' : 'release_date',
# 	'species_count' : 'SpeciesCount',
# 	'species_est' : 'SpeciesEst',
# 	'author_or_editor' : 'author_or_editor',
# 	'accepted_species_names' : 'accepted_species_names',
# 	'accepted_infraspecies_names' : 'accepted_infraspecies_names',
# 	'species_synonyms' : 'species_synonyms',
# 	'infraspecies_synonyms' : 'infraspecies_synonyms',
# 	'common_names' : 'common_names',
# 	'total_names' : 'total_names',
# }

# Create your models here.
class Database(models.Model):
	name = models.CharField(max_length=200)
	full_name = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	contact_person = models.CharField(max_length=200)
	taxa = models.CharField(max_length=200)
	taxonomic_converage = models.CharField(max_length=200)
	abstract = models.CharField(max_length=200)
	version = models.CharField(max_length=200)
	release_date = models.CharField(max_length=200)
	organization = models.CharField(max_length=200)
	species_est = models.IntegerField(10)
	authors_editors = models.CharField(max_length=200)
	accepted_species_names = models.IntegerField(10)
	accepted_infraspecies_names = models.IntegerField(10)
	species_synonyms = models.IntegerField(10)
	infraspecies_synoyms = models.IntegerField(10)
	common_names = models.IntegerField(10)
	total_names = models.IntegerField(10)
	species_count = models.IntegerField(10)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
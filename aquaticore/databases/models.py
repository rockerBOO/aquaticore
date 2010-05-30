from django.db import models

# Create your models here.
class Database(models.Model):
	name                        = models.CharField(max_length=200)
	full_name                   = models.CharField(max_length=200)
	display_name                = models.CharField(max_length=200)
	link                        = models.CharField(max_length=200)
	contact_person              = models.CharField(max_length=200)
	taxa                        = models.CharField(max_length=200)
	taxonomic_coverage          = models.TextField()
	abstract                    = models.TextField()
	version                     = models.CharField(max_length=200)
	release_date                = models.CharField(max_length=200)
	organization                = models.TextField()
	species_est                 = models.IntegerField(10)
	authors_editors             = models.TextField()
	accepted_species_names      = models.IntegerField(10)
	accepted_infraspecies_names = models.IntegerField(10)
	species_synonyms            = models.IntegerField(10)
	infraspecies_synonyms       = models.IntegerField(10)
	common_names                = models.IntegerField(10)
	total_names                 = models.IntegerField(10)
	species_count               = models.IntegerField(10)
	created                     = models.DateTimeField('date published')
	modified                    = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
from django.db import models

# Create your models here.
class Author(models.Model):
	title = models.CharField(max_length=200)
	source = models.CharField(max_length=200)
	country = models.ForeignKey('geography.Country')
	year = models.DateField()
	database = models.ForeignKey('databases.Database')
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
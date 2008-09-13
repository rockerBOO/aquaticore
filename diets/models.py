from django.db import models

class Diet(models.Model):
	DIET_CHOICES = (
	    ('F', 'Frozen'),
	    ('L', 'Live'),
		('D', 'Dry'),
		('Q', 'Liquid'),
	)
	
	title = models.CharField(max_length=200)
	material_type = models.CharField(max_length=1, choices=DIET_CHOICES)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
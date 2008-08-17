from django.db import models

class Fish:
	title   = models.CharField(max_length=200)
    body    = models.TextField()
    created = models.DateTimeField('date published')

	def __unicode__(self):
        return self.title
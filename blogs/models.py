from django.db import models
import datetime

class Blog(models.Model):
    title   = models.CharField(max_length=200)
    body    = models.TextField()
    created = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.title
        
    def was_created_today(self):
        return self.created.date() == datetime.date.today()
        
from django.contrib import admin

admin.site.register(Blog)

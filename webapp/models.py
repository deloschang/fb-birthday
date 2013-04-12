from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=180, blank=True)
    uid = models.BigIntegerField(blank=True)
    birthday = models.CharField(max_length=180, blank=True)

    def __unicode__(self):
        return self.name
    



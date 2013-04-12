from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=180, blank=True)
    #uid = models.IntegerField(blank=True)
    #birthday = models.DateField(blank=True)

    def __unicode__(self):
        return self.name
    



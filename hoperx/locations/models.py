from django.db import models


class LocationType(models.Model):
    description = models.CharField(max_length=40)

    def __unicode__(self):
        return self.description


class Location(models.Model):
    name = models.CharField(max_length=100)
    location_type = models.ForeignKey(LocationType,related_name='locations')
    slug = models.SlugField()
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class LocationAttributes(models.Model):
    location = models.ForeignKey(Location)
    field_name = models.CharField(max_length=100)
    field_value = models.TextField()

    def __unicode__(self):
        return '%s : %s' % self.field_name, self.field_value
    
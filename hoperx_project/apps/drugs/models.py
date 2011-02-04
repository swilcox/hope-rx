from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class DrugForm(models.Model):
    name = models.CharField(max_length=50,primary_key=True)

    def __unicode__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=30)
    plural_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Drug(models.Model):
    medicine = models.CharField(max_length=100,db_index=True)
    form = models.ForeignKey(DrugForm)
    strength = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    measurement = models.ForeignKey(Unit)
    default_buy_quantity = models.IntegerField(default=1)
    default_dispense_quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s %s %s' % self.medicine, self.form, self.strength

    
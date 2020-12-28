from django.db import models


class CountryGroup(models.Model):
    '''
    Stores the names of country groups
    Related by :model: `dataloader.PopulationData`
    '''

    country_group = models.CharField(max_length=100)

    class Meta:
        ordering = ['country_group']

    def __str__(self):
        return f"{self.country_group}"


class PopulationData(models.Model):
    '''
    Represents the database model
    group references many to many relation with
    :model: `dataloader.CountryGroup`
    '''

    country = models.CharField(max_length=100)
    code = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    population = models.FloatField(blank=False)
    group = models.ManyToManyField(CountryGroup)

    def __str__(self):
        return f"{self.country}, {self.code},\
        {self.year}, {self.population}, {self.group}"

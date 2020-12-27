from django.db import models


class CountryGroup(models.Model):
    country_group = models.CharField(max_length=100)

    class Meta:
        ordering = ['country_group']

    def __str__(self):
        return f"{self.country_group}"


class PopulationData(models.Model):
    country = models.CharField(max_length=100)
    code = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    population = models.FloatField(blank=False)
    group = models.ManyToManyField(CountryGroup)

    def __str__(self):
        return f"{self.country}, {self.code},\
        {self.year}, {self.population}, {self.group}"

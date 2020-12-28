from django.core.management.base import BaseCommand, CommandError
from dataloader.models import PopulationData, CountryGroup
import csv
import os
from django.apps import apps
from ._private import Regions


class Command(BaseCommand):
    """
    Custom command code to load database from csv file
    Populates the main model and multi relations model
    """

    help = 'collects data from csv and loads to database'

    def add_arguments(self, parser):
        pass

    def get_csv(self, csv_file):
        """ function to get the path to the csv file """
        path = apps.get_app_config('dataloader').path
        file_path = os.path.join(path, "csvdata", csv_file)
        return file_path

    def handle(self, *args, **options):
        """
        Handler function that loops through the csv
        populates the tables based on conditions
        """
        g_saarc = CountryGroup(country_group='SAARC')
        g_saarc.save()
        g_asean = CountryGroup(country_group='ASEAN')
        g_asean.save()
        g_g4 = CountryGroup(country_group='G4')
        g_g4.save()
        g_brics = CountryGroup(country_group='BRICS')
        g_brics.save()
        g_g7 = CountryGroup(country_group='G7')
        g_g7.save()

        # obtains the path to csv file
        path = self.get_csv('popest.csv')

        try:
            with open(path, 'r') as newfile:
                csv_read = csv.reader(newfile, delimiter=',')
                for line in csv_read:
                    data = PopulationData(
                            country=line[0],
                            code=line[1],
                            year=line[2],
                            population=line[3],
                        )
                    data.save()
                    if line[0] in Regions.saarc:
                        data.group.add(g_saarc)

                    if line[0] in Regions.asean:
                        data.group.add(g_asean)

                    if line[0] in Regions.g4:
                        data.group.add(g_g4)

                    if line[0] in Regions.brics:
                        data.group.add(g_brics)

                    if line[0] in Regions.g7:
                        data.group.add(g_g7)

        except FileNotFoundError:
            raise CommandError("File does not exist")

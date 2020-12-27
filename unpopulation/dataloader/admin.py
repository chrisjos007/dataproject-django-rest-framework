from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

# Register your models here.
from .models import PopulationData, CountryGroup


@admin.register(PopulationData)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ("country", "code", "year", "population", "get_group")
    list_filter = (
        ("country", DropdownFilter),
        ("code", DropdownFilter),
        ("year", DropdownFilter),
    )
    search_fields = ("country__startswith", "code__startswith")

    def get_group(self, obj):
        return "\n".join([a.country_group for a in obj.group.all()])


@admin.register(CountryGroup)
class ContryGroupAdmin(admin.ModelAdmin):
    list_display = ("country_group", "get_group")

    def get_group(self, obj):
        return "\n".join([a.country for a in obj.populationdata_set.all().distinct('country')])

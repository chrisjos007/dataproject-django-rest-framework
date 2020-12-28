from django.shortcuts import render
from .serializers import FirstSerializer, SecondSerializer
from .models import PopulationData, CountryGroup
import json
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def first_view(request):
    country_data = PopulationData.objects.all().values('country').distinct()
    year_data = PopulationData.objects.all().values('year').distinct()
    countries = list()
    years = list()
    for entry in country_data:
        countries.append(entry['country'])
    for entry in year_data:
        years.append(entry['year'])
    years = sorted(years)
    return render(
        request, 'first.html',
        {'countries': countries, 'start': years[:-5:], 'end': years[5::]}
        )


@api_view(['GET', 'POST'])
@csrf_exempt
def first(request):
    if request.method == 'GET':
        queryset = PopulationData.objects.all()[0:50]
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        data = json.loads(request.body)
        country = data["country"]
        startyear = int(data["start"])
        endyear = int(data["end"])

        queryset = PopulationData.objects.all().\
            filter(country=country, year__range=(startyear, endyear))
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
def second_view(request):
    country_group = CountryGroup.objects.all()
    year_data = PopulationData.objects.all().values('year').distinct()
    groups = list()
    years = list()
    for entry in country_group:
        groups.append(entry.country_group)
    for entry in year_data:
        years.append(entry['year'])
    years = sorted(years)
    return render(request, 'second.html', {'groups': groups, 'years': years})


@api_view(['GET', 'POST'])
@csrf_exempt
def second(request):
    if request.method == 'GET':
        queryset = PopulationData.objects.all()[0:50]
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        data = json.loads(request.body)
        group_data = data["group"]
        year = int(data["year"])
        group_obj = CountryGroup.objects.\
            filter(country_group=group_data).first()
        queryset = PopulationData.objects.all().\
            filter(year=year, group=group_obj)
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
def third_view(request):
    country_group = CountryGroup.objects.all()
    year_data = PopulationData.objects.all().values('year').distinct()
    groups = list()
    years = list()
    for entry in country_group:
        groups.append(entry.country_group)
    for entry in year_data:
        years.append(entry['year'])
    years = sorted(years)
    return render(
        request, 'third.html',
        {'groups': groups, 'start': years[:-5:], 'end': years[5::]}
        )


@api_view(['GET', 'POST'])
@csrf_exempt
def third(request):
    if request.method == 'GET':
        queryset = PopulationData.objects.values('year').\
            annotate(total_population=Sum('population')).order_by('year')
        serializer = SecondSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        data = json.loads(request.body)
        group_data = data["group"]
        startyear = int(data["start"])
        endyear = int(data["end"])
        group_obj = CountryGroup.objects.\
            filter(country_group=group_data).first()
        queryset = PopulationData.objects.values('year').\
            filter(group=group_obj, year__range=(startyear, endyear)).\
            annotate(total_population=Sum('population')).order_by('year')
        serializer = SecondSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt
def fourth_view(request):
    country_group = CountryGroup.objects.all()
    year_data = PopulationData.objects.all().values('year').distinct()
    groups = list()
    years = list()
    for entry in country_group:
        groups.append(entry.country_group)
    for entry in year_data:
        years.append(entry['year'])
    years = sorted(years)
    return render(
        request, 'fourth.html',
        {'groups': groups, 'start': years[:-5:], 'end': years[5::]}
        )


@api_view(['GET', 'POST'])
@csrf_exempt
def fourth(request):
    if request.method == 'GET':
        queryset = PopulationData.objects.\
            values('country', 'population', 'year').\
            order_by('year').all()[0:20]
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        data = json.loads(request.body)
        group_data = data["group"]
        startyear = int(data["start"])
        endyear = int(data["end"])
        group_obj = CountryGroup.objects.\
            filter(country_group=group_data).first()
        queryset = PopulationData.objects.\
            values('country', 'population', 'year').\
            filter(group=group_obj, year__range=(startyear, endyear)).\
            order_by('year')
        serializer = FirstSerializer(queryset, many=True)
        return Response(serializer.data)

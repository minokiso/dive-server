from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from Utils.viewset import ModelViewSetPlus
from athlete.models import Athlete
from athlete.serializer import AthleteSerializer
import requests
# Create your views here.
from medal.models import Medal
from medal.serializer import MedalSerializer


class MedalView(APIView):
    def get(self, request, *args, **kwargs):
        medals = Medal.objects.all()
        serializer = MedalSerializer(instance=medals, many=True)
        return Response(serializer.data)

    def _post(self, request, *args, **kwargs):
        raw_medals = get_medal()
        medals = []
        for raw_medal in raw_medals:
            medal = Medal(
                Rank=raw_medal.get('Rank'),
                CountryName=raw_medal.get('CountryName'),
                CountryCode=raw_medal.get('CountryCode'),
                TotalCount=raw_medal.get('TotalCount'),
                Gold=raw_medal.get('Gold').get('Count'),
                Silver=raw_medal.get('Gold').get('Count'),
                Bronze=raw_medal.get('Gold').get('Count'),
            )
            medals.append(medal)
        Medal.objects.bulk_create(medals)
        return Response(raw_medals)


def get_medal():
    url = 'https://api.worldaquatics.com/fina/competitions/3337/medals'
    params = {}

    response = requests.get(url, params=params)
    raw_medals = response.json()
    _raw_medals = raw_medals.get("Medals").get('SportMedals')[0].get("Countries")

    return _raw_medals

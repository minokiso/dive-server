from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from Utils.viewset import ModelViewSetPlus
from athlete.models import Athlete
from athlete.serializer import AthleteSerializer
import requests


class AthleteView(APIView):
    def get(self, request, *args, **kwargs):
        athletes = Athlete.objects.all()
        serializer = AthleteSerializer(instance=athletes, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        ResultId = request.data.get('ResultId')
        athlete = Athlete.objects.filter(ResultId=ResultId).first()
        if athlete:
            print(athlete.image)
            return Response(athlete.image)
        return Response(None)

    def _post(self, request, *args, **kwargs):
        raw_athletes = get_raw_athletes()
        athletes = []
        for contry in raw_athletes:
            for raw_athlete in contry.get('Participations'):
                athlete = Athlete(
                    CountryName=contry.get("CountryName"),
                    CountryCode=contry.get("CountryCode"),
                    LastName=raw_athlete.get('PreferredLastName'),
                    FirstName=raw_athlete.get('PreferredFirstName'),
                    Gender=raw_athlete.get('Gender'),
                    DBO=raw_athlete.get('DBO'),
                    ResultId=raw_athlete.get('ResultId'),
                    image=get_image(raw_athlete.get('ResultId'))
                )

                athletes.append(athlete)
        Athlete.objects.bulk_create(athletes)
        return Response(raw_athletes)


def get_raw_athletes():
    url = 'https://api.worldaquatics.com/fina/competitions/3337/athletes'
    params = {}

    response = requests.get(url, params=params)
    raw_athletes = response.json()
    return raw_athletes


def get_image(ResultId):
    url = f'https://api.worldaquatics.com/content/fina/photo/en/?pageSize=1&tagNames=athlete-image&referenceExpression=%22FINA_ATHLETE:{ResultId}%22'
    response = requests.get(url)
    image_info = response.json().get("content")
    if len(image_info) > 0:
        image_url = image_info[0].get("onDemandUrl") + "?width=80"
        print(image_url)
        return image_url
    return None

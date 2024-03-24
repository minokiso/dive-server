from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from Utils.viewset import ModelViewSetPlus
from athlete.models import Athlete
from athlete.serializer import AthleteSerializer
import requests

# Create your views here.
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer


class ScheduleView(APIView):
    def get(self, request, *args, **kwargs):
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(instance=schedules, many=True)
        return Response(serializer.data)

    def _post(self, request, *args, **kwargs):
        raw_schedules = get_raw_schedules()
        schedules = []
        for raw_schedule in raw_schedules:
            schedule = Schedule(
                Date=raw_schedule.get("Date"),
                name=raw_schedule.get("DisciplineName"),
                type=raw_schedule.get("PhaseName"),
                DisciplineId=raw_schedule.get("DisciplineId"),
                UtcDateTime=raw_schedule.get("UtcDateTime"),
            )
            schedules.append(schedule)
        Schedule.objects.bulk_create(schedules)
        return Response(raw_schedules)

    def _put(self, request, *args, **kwargs):
        schedules = Schedule.objects.all()
        results = {}
        for schedule in schedules:
            if schedule.DisciplineId not in results:
                results[schedule.DisciplineId] = get_results(schedule.DisciplineId)
            result = next(
                (result.get('Results') for result in results[schedule.DisciplineId] if result.get("PhaseName") == schedule.type), None)
            schedule.Result = result
            schedule.save()
        serializer = ScheduleSerializer(instance=schedules, many=True)
        return Response(serializer.data)
        # return Response(results)


def get_raw_schedules():
    url = 'https://api.worldaquatics.com/fina/competitions/3337/schedule'
    params = {}

    response = requests.get(url, params=params)
    raw_schedules = response.json()
    return raw_schedules


def get_results(discipline_id):
    url = f'https://api.worldaquatics.com/fina/events/{discipline_id}'
    params = {}

    response = requests.get(url, params=params)
    result = response.json()
    return result.get("Heats")

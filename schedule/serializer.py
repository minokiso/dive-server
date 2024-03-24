from rest_framework import serializers

from athlete.models import Athlete
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Schedule

from rest_framework import serializers

from athlete.models import Athlete


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Athlete
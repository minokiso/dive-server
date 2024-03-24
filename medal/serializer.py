from rest_framework import serializers

from athlete.models import Athlete
from medal.models import Medal


class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Medal
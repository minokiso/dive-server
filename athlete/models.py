from django.db import models


# Create your models here.
# {
#   "CountryName": "Austria",
#   "CountryCode": "AUT",
#   "Participations": [
#     {
#       "ResultId": 1057040,
#       "Gender": 0,
#       "PreferredLastName": "HART",
#       "PreferredFirstName": "Alexander",
#       "ScoreboardPhotoId": "c71d6025-9088-4aae-b276-a9416f1cd115",
#       "Sports": "DV",
#       "DOB": "1999-03-07T00:00:00",
#       "NAT": "Austria",
#       "Disciplines": [
#         {
#           "DisciplineId": "e85aed35-be49-4251-9558-a4b651f57266",
#           "DisciplineCode": "002",
#           "DisciplineName": "Men 3m Springboard",
#           "PhaseId": "3abd8d45-1c15-4bf9-94c8-7ebc1f3ec42e",
#           "PhaseCode": "100",
#           "PhaseName": "Finals",
#           "HeatName": "Final"
#         },
#         {
#           "DisciplineId": "6119565c-9b6a-429a-ac0d-183a7fd37e55",
#           "DisciplineCode": "202",
#           "DisciplineName": "Men 3m Synchronised",
#           "PhaseId": "3abd8d45-1c15-4bf9-94c8-7ebc1f3ec42e",
#           "PhaseCode": "100",
#           "PhaseName": "Finals",
#           "HeatName": "Final"
#         }
#       ]
#     },
#   ]
# }
class Athlete(models.Model):
    CountryName = models.CharField(max_length=255, blank=True, null=True)
    CountryCode = models.CharField(max_length=255, blank=True, null=True)
    FirstName = models.CharField(max_length=255, blank=True, null=True)
    LastName = models.CharField(max_length=255, blank=True, null=True)
    DBO = models.CharField(max_length=255, blank=True, null=True)
    Gender = models.SmallIntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    ResultId = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'athlete'

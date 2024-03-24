from django.db import models


# Create your models here.
# {
#   "Name": "Preliminary",
#   "Date": "2024-01-18",
#   "Time": "10:00:00",
#   "UtcDateTime": "2024-01-18T09:00:00",
#   "Day": 1,
#   "UtcDay": 1,
#   "DisciplineName": "Women 1m Springboard",
#   "PhaseName": "Preliminaries",
#   "HeatUnit": "01",
#   "ResultStatus": "OFFICIAL",
#   "SportId": "7306cbfb-2d8a-4f69-998b-a03b8c1e5115",
#   "DisciplineId": "108c795d-5e4f-4dc6-acea-0bc70bfd1928",
#   "SportCode": "DV",
#   "TimeZone": "01:00:00",
#   "TimeZoneDisplayName": "W. Europe Standard Time"
# }
class Schedule(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    DisciplineId = models.CharField(max_length=255, blank=True, null=True)
    UtcDateTime = models.CharField(max_length=255, blank=True, null=True)
    Date = models.CharField(max_length=255, null=True, blank=True)
    Result = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'schedule'

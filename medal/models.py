from django.db import models


# Create your models here.
class Medal(models.Model):
    Rank = models.IntegerField(null=True, blank=True)
    CountryName = models.CharField(max_length=255, blank=True, null=True)
    CountryCode = models.CharField(max_length=255, blank=True, null=True)
    TotalCount = models.IntegerField(null=True, blank=True)
    Gold = models.IntegerField(null=True, blank=True)
    Silver = models.IntegerField(null=True, blank=True)
    Bronze = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'metal'

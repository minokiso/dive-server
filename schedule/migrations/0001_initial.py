# Generated by Django 4.2.11 on 2024-03-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('DisciplineId', models.CharField(blank=True, max_length=255, null=True)),
                ('UtcDateTime', models.CharField(blank=True, max_length=255, null=True)),
                ('Result', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_clubs_placements_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='file',
            field=models.FileField(default='resume..pdf', upload_to='uploads/%m-%Y/'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-14 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therulz', '0007_auto_20180613_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_player_count',
            field=models.IntegerField(default=0),
        ),
    ]
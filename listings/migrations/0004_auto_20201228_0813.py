# Generated by Django 3.1.4 on 2020-12-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20201228_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=200),
        ),
    ]

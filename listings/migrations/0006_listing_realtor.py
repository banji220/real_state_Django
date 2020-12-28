# Generated by Django 3.1.4 on 2020-12-28 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20201224_1205'),
        ('listings', '0005_auto_20201228_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]

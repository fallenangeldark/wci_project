# Generated by Django 2.0.7 on 2018-11-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp_ru', '0016_auto_20181113_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innerhomeru',
            name='h1',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
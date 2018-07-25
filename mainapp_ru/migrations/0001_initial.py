# Generated by Django 2.0.7 on 2018-07-24 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeRu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('h1', models.CharField(blank=True, max_length=30)),
                ('paragraph1', models.TextField(blank=True)),
                ('paragraph2', models.TextField(blank=True)),
                ('paragraph3', models.TextField(blank=True)),
                ('paragraph4', models.TextField(blank=True)),
                ('paragraph5', models.TextField(blank=True)),
                ('paragraph6', models.TextField(blank=True)),
                ('paragraph7', models.TextField(blank=True)),
                ('paragraph8', models.TextField(blank=True)),
                ('paragraph9', models.TextField(blank=True)),
                ('paragraph10', models.TextField(blank=True)),
                ('paragraph11', models.TextField(blank=True)),
                ('paragraph12', models.TextField(blank=True)),
                ('paragraph13', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='InnerHomeRu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('h2', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Вложенные страницы',
            },
        ),
        migrations.CreateModel(
            name='Professionals_ru',
            fields=[
                ('innerhomeru_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp_ru.InnerHomeRu')),
            ],
            bases=('mainapp_ru.innerhomeru',),
        ),
        migrations.AddField(
            model_name='innerhomeru',
            name='outer_relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp_ru.HomeRu'),
        ),
    ]

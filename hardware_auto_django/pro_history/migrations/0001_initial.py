# Generated by Django 4.2.4 on 2023-11-29 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_text', models.CharField(max_length=200)),
                ('project_date', models.DateTimeField(verbose_name='project exe date')),
                ('project_auth', models.CharField(max_length=200)),
            ],
        ),
    ]
# Generated by Django 3.1.4 on 2021-01-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(help_text='formato: YYYY-MM-DD'),
        ),
    ]
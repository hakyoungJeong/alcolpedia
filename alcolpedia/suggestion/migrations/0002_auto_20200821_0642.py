# Generated by Django 3.0.8 on 2020-08-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggetion',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

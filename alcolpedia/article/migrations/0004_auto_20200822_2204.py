# Generated by Django 3.0.8 on 2020-08-22 13:04

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_content_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='body',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='summary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='hashtag', to='article.Tag'),
        ),
    ]

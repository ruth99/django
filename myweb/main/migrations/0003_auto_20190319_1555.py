# Generated by Django 2.1.5 on 2019-03-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190318_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 2.2 on 2020-12-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataloader', '0004_auto_20201220_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='populationdata',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]

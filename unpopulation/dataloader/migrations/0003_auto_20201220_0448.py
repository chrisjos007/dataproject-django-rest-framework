# Generated by Django 2.2 on 2020-12-20 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataloader', '0002_auto_20201220_0447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='populationdata',
            old_name='region',
            new_name='group',
        ),
    ]

# Generated by Django 2.2.19 on 2022-05-11 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220512_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='title',
        ),
    ]

# Generated by Django 2.2.19 on 2022-05-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_group_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(default=str, max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='simple projet; un projet de test'),
            preserve_default=False,
        ),
    ]

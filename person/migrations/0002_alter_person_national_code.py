# Generated by Django 5.1 on 2024-08-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='national_code',
            field=models.IntegerField(default='0010', max_length=10, unique=True),
        ),
    ]

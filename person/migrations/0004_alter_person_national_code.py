# Generated by Django 5.1 on 2024-08-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_national_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='national_code',
            field=models.CharField(default='0010000000', max_length=10),
        ),
    ]

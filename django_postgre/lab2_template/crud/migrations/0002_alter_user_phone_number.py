# Generated by Django 4.1.4 on 2022-12-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveBigIntegerField(max_length=11, null=True),
        ),
    ]
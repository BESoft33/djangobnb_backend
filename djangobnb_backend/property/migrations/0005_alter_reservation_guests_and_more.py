# Generated by Django 5.0.2 on 2024-03-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_property_bathrooms_alter_property_bedrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guests',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_nights',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

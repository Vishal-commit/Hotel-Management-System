# Generated by Django 5.1.1 on 2024-09-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='price_per_night',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')], max_length=10),
        ),
    ]

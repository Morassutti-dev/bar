# Generated by Django 5.1.6 on 2025-02-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_alter_itemcomanda_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

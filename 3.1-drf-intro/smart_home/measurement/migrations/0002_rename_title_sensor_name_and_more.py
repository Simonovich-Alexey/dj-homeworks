# Generated by Django 5.0 on 2023-12-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
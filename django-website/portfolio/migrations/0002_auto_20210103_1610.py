# Generated by Django 3.1.4 on 2021-01-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='linked_data',
            field=models.JSONField(blank=True, help_text='Linked Data in JSON', null=True),
        ),
    ]

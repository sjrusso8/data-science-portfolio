# Generated by Django 3.1.4 on 2021-01-03 16:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='linked_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Linked Data in JSON', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='payoff',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Home intro'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='works_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='works_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
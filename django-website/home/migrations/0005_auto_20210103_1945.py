# Generated by Django 3.1.4 on 2021-01-03 19:45

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210103_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='partner_subtitle',
            new_name='about_subtitle',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='partner_title',
            new_name='about_title',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='works_subtitle',
            new_name='portfolio_subtitle',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='works_title',
            new_name='portfolio_title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='payoff',
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Home Subtitle'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Home Subtitle'),
        ),
    ]

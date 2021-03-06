# Generated by Django 3.1.4 on 2021-01-04 20:29

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0059_apply_collection_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('section_title', wagtail.core.fields.RichTextField(blank=True)),
                ('section_subtitle', wagtail.core.fields.RichTextField(blank=True)),
                ('linked_data', models.JSONField(blank=True, help_text='Linked Data in JSON', null=True)),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(blank=True, default='', max_length=100)),
                ('description', wagtail.core.fields.RichTextField()),
                ('story', wagtail.core.fields.RichTextField()),
                ('link', models.URLField(blank=True, help_text='Project link', null=True)),
                ('git_link', models.URLField(blank=True, help_text='Github link', null=True)),
                ('show_in_home', models.BooleanField(default=False)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='portfolio.portfoliopage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_portfoliotags_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='portfolio.PortfolioTags', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

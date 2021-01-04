# Generated by Django 3.1.4 on 2021-01-04 20:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('portfolio', '0002_auto_20210104_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
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
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='category',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='git_link',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='link',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='show_in_home',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='story',
        ),
        migrations.RemoveField(
            model_name='portfoliopage',
            name='tags',
        ),
        migrations.DeleteModel(
            name='PortfolioTags',
        ),
        migrations.AddField(
            model_name='project',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.portfoliopage'),
        ),
    ]

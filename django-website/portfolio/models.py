from django.db import models
from django.utils.translation import ugettext as _

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from core.models import BaseModel


class PortfolioPage(BaseModel):
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('section_title'),
                FieldPanel('section_subtitle'),
                InlinePanel('projects', label=_('projects')),
            ],
            heading=_('Works')
        ),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('linked_data'),
    ]
class Project(Orderable):
    page = ParentalKey(PortfolioPage, related_name='projects')
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, default='', blank=True)
    description = RichTextField()
    story = RichTextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+')
    link = models.URLField(help_text=_('Project link'), null=True, blank=True)
    git_link = models.URLField(help_text=_('Github link'), null=True, blank=True)

    # make the project visible in the homepage
    show_in_home = models.BooleanField(default=False)

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image'),
        FieldPanel('link'),
        FieldPanel('git_link'),
        FieldPanel('category'),
        FieldPanel('description'),
        FieldPanel('story'),
        FieldPanel('show_in_home'),
    ]
from django.db import models
from django.utils.translation import ugettext as _

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from core.models import BaseModel

class PostPage(BaseModel):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('section_title'),
        FieldPanel('section_subtitle'),
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]
from django.db import models
from django.utils.translation import ugettext as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
# from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
# from wagtail.images.edit_handlers import ImageChooserPanel

from core.models import BaseModel
from portfolio.models import Project

class HomePage(BaseModel):
    main_subtitle = RichTextField(blank=True, help_text=_('Home Subtitle'))
    main_description = RichTextField(blank=True, help_text=_('Home Subtitle'))

    portfolio_title = RichTextField(blank=True)
    portfolio_subtitle = RichTextField(blank=True)

    about_title = RichTextField(blank=True)
    about_subtitle = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('main_subtitle'),
                FieldPanel('main_description'),
            ],
            heading=_('Main Heading')
        ),

        MultiFieldPanel(
            [
                FieldPanel('portfolio_title'),
                FieldPanel('portfolio_subtitle'),
            ],
            heading=_('Portfolio')
        ),

        MultiFieldPanel(
            [
                FieldPanel('about_title'),
                FieldPanel('about_subtitle'),
            ],
            heading=_('About Me')
        ),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('linked_data'),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['projects'] = Project.objects.filter(show_in_home=True)
        context['minor_projects'] = Project.objects.filter(show_in_home=False)
        return context

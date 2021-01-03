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
    payoff = RichTextField(blank=True, help_text=_('Home intro'))

    partner_title = RichTextField(blank=True)
    partner_subtitle = RichTextField(blank=True)

    works_title = RichTextField(blank=True)
    works_subtitle = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('payoff'),

        MultiFieldPanel(
            [
                FieldPanel('section_title'),
                FieldPanel('section_subtitle'),
            ],
            heading=_('Services')
        ),

        MultiFieldPanel(
            [
                FieldPanel('works_title'),
                FieldPanel('works_subtitle'),
            ],
            heading=_('Works')
        ),

    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('linked_data'),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['projects'] = Project.objects.filter(show_in_home=True)
        return context

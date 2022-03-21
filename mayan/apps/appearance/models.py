import bleach

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mayan.apps.events.classes import EventManagerSave
from mayan.apps.events.decorators import method_event

from .events import event_theme_created, event_theme_edited
from colorful.fields import RGBColorField

status = (
    ('On','On'),
    ('Off', 'Off'),
)

class Theme(ExtraDataModelMixin, models.Model):
    label = models.CharField(
        db_index=True, help_text=_('A short text describing the theme.'),
        max_length=128, unique=True, verbose_name=_('Label')
    )

    # Add url to change logo
    logo = models.TextField(
        blank=True, help_text=_(
            'The url to change your logo.'
        ), verbose_name=_('Logo'),
        default="https://lh3.googleusercontent.com/fife/AAWUweULhkCLGFq9L8BUSFYnuWiRPhSp-dpqSnrRy3SlPKxp8u3Uiq_r_4otrCDMwaedmJZWi-9wgbTMtjQftF_n52djRhB84Ccosq93jAbSM4krlnVY4RxFUV02tsHSEjDy9pEcR8pyujKvJ47iwN_-Cn9h6f3jx7vhBXJY9pNtsss6uuuwjGitbGJbuka85LOhfmsLUPl_nWueZjo38mbtn2zFcBoGm-1-cqRQKClc6EzuhCSfK8R2Z17w969ix7f6dPQz7zNLlICtQa-yVTM_1Q-n7pYRDjSeKLsLybHKHSBOHi3755-uOQiA7wnj-_QCmVcSMYuWIid0Ih22AO8fUDtcLndssboU-Ne41XyY9v8mp0egQ4wYEn6QphN-9OR0m0mbf8yYSJpQ62ysiVPvsG671s25mlgnoiFmXeP2h2HLfPO2jVO4cYhzD1nV1Fvm5ACAJp9i0GVvuigDO4CB0sA20traVLs4R8oI9U5mwp48xsZYGz02Ib6whyKqZ8Bzb0K5T3su-bcE_OpCj4EpiJaG9O6A6syElXLCQPno_4RR9nijcEgtH2OVmz2a3SauETpOYnjbe3PisK8RnZBK7HIaB9k-LM8JrxEVBvvKG5Y7lFIsxkmg-JXlLFLCBzbSt_ys07Nari9AdCjSrBRVBgwy5X1cdqIAIHjSM1iJi1gZOJP6yLi6z6K5fp3Za86-DTJWnJR9PWvSUoyoijv5kfsHzF5f8ZVdWw=w1920-h955"
    )

    stylesheet = models.TextField(
        blank=True, help_text=_(
            'The CSS stylesheet to change the appearance of the different '
            'user interface elements.'
        ), verbose_name=_('Stylesheet')
    )

    navbarcolor = RGBColorField(
        blank=True, 
        help_text=_('Choose a color to change the navbar.'), 
        verbose_name=_('Navbar Color')
    )

    menucolor = RGBColorField(
        blank=True, 
        help_text=_('Choose a color to change the Menu.'),
        verbose_name=_('Menu Color')
    )

    statustheme = models.CharField(
        max_length=100,
        choices=status,
        default=status[1][0],
        verbose_name=_('Status Theme')
    )

    class Meta:
        ordering = ('label',)
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __str__(self):
        return force_text(s=self.label)

    def get_absolute_url(self):
        return reverse(
            viewname='appearance:theme_edit', kwargs={
                'theme_id': self.pk
            }
        )

    @method_event(
        event_manager_class=EventManagerSave,
        created={
            'event': event_theme_created,
            'target': 'self',
        },
        edited={
            'event': event_theme_edited,
            'target': 'self',
        }
    )
    def save(self, *args, **kwargs):
        self.stylesheet = bleach.clean(
            text=self.stylesheet, tags=('style',)
        )
        if(self.status_theme == "On"):
           obj = Theme.objects.filter(status_theme='On').update(status_theme='Off')
        super().save(*args, **kwargs)


class UserThemeSetting(models.Model):
    user = models.OneToOneField(
        on_delete=models.CASCADE, related_name='theme_settings',
        to=settings.AUTH_USER_MODEL, verbose_name=_('User')
    )
    theme = models.ForeignKey(
        blank=True, null=True, on_delete=models.CASCADE,
        related_name='user_setting', to=Theme, verbose_name=_('Theme')
    )

    class Meta:
        verbose_name = _('User theme setting')
        verbose_name_plural = _('User theme settings')

    def __str__(self):
        return force_text(s=self.user)

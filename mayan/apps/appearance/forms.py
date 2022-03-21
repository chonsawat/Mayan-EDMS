from django import forms

from mayan.apps.views.forms import DetailForm

from .models import Theme, UserThemeSetting


class ThemeForm(forms.ModelForm):
    class Meta:
        fields = ('label', 'logo','stylesheet','navbarcolor','menucolor','status_theme')
        model = Theme


class UserThemeSettingForm(forms.ModelForm):
    class Meta:
        fields = ('theme',)
        model = UserThemeSetting
        widgets = {
            'theme': forms.Select(
                attrs={
                    'class': 'select2'
                }
            ),
        }


class UserThemeSettingForm_view(DetailForm):
    class Meta:
        fields = ('theme',)
        model = UserThemeSetting

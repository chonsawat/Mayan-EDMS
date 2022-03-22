from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template import Library
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from ..literals import COMMENT_APP_TEMPLATE_CACHE_DISABLE

# Chonsawat TODO:
from ..models import Theme

app_templates_cache = {}
register = Library()

@register.simple_tag
def get_theme_context_default():
    try:
        logo = f"{Theme.objects.get(id=1).logo}"
    except:
        print(f"Chonsawat aleart at: apps/appearance/templatetags/appearance_tags.py in get_logo_default")
        return ''

    return f"{logo}|{logo}"

def create_or_load_default_theme():
    default_id_create_or_load = 1
    create_logo = 'https://lh3.googleusercontent.com/fife/AAWUweUyRNSI4L_WQCZ75M6G2ddiKyXGDXdUMn3Y4pyDjC9-x3j9sFwyGM7QYLkMbvyPqTaNaoVmMBNKVMPHMZ9qYMW8G0SCWCtAu9_m2xMd5pyS50vbMrgsW_waEBwTG1_zBY6y4QUQzXXkU6dibFrhjRXjKg18g-mTOLI_94dvwDWcZ7KInpe2qjHNwxexJnL_w8hYt1Ue7Iu_ANEkp3Eed4bzZOmRl2OTc_vQIHXr4m_BgrzWVCiii_iiGKkiDUzxTbBGerQjLCru8JGs2XTQZ0uyGLk2b5rvryDX0Uj-vdHTkQQLya5mcwiFcO3LqUdTXtxGoBz_fxNMzQPAZS4xOp9A-tzXtnA1z3Mj5aEu7Zay3uv7qlj_KHYfptV4Y1DLcZiGgBIPVsBkjJX7fXsgzNuCaYWEimsZLdJHF2pQKktXEf1Pf2QVJN_TSsdaPvgMVNGr56s1V3tGEzHmLBxOKwJdxxpEDv-55EBG2J-0QyuCy483Nn1-ELLoJoxv78z_ZbsmwuiCA9MtJdteiH4AIwaJcrGfz_PQ3bLyeQzcGUlylH8vwrewb12WbjDz6arTj0ZOYDYD_eslmILW7PWQLyiLqXPCZFwjwFbr66mFUq5HtrPvoARlNkoiUsFUvgPdj7witCPXDunuNJbcHts2QkYx-fh3YmuFFBGONKYW8uSCohpNzFJm53FtTyh9EVMFPXZnA6qUoy_bdsgWSliJi5fwx-5jO_kfRYYnw0nhnsa6GX5cSikIvNTXymBBwNEJMEUoQSPTaXK9KzvOiBTZ2uVkPdAUl9Cfry6Ym8Rn_as=w1920-h933'
    try:
        Theme.objects.get(id=default_id_create_or_load)
        print(f"Load: {Theme.objects.get(id=default_id_create_or_load)} Theme")
    except:
        Theme.objects.create(id=default_id_create_or_load, label='Original', logo=create_logo)
        print(f"Create: {Theme.objects.get(id=default_id_create_or_load)} Theme")


create_or_load_default_theme()


@register.simple_tag(takes_context=True)
def appearance_app_templates(context, template_name):
    """
    Fetch the app templates for the requested `template_name`, render it with
    the current `request` from the `context`, and cache it for future use
    unless the template has the no caching comment.
    """
    result = []

    for app in apps.get_app_configs():
        template_id = '{}.{}'.format(app.label, template_name)
        if template_id not in app_templates_cache or settings.DEBUG:
            try:
                app_template = get_template(
                    '{}/app/{}.html'.format(app.label, template_name)
                )
                context['custom_logo_django'] = get_theme_context_default().split('|')[0]
                app_template_output = app_template.render(
                    request=context.get('request')
                )

                if COMMENT_APP_TEMPLATE_CACHE_DISABLE not in app_template.template.source:
                    app_templates_cache[template_id] = app_template_output
            except TemplateDoesNotExist:
                """
                Non fatal just means that the app did not defined an app
                template of this name and purpose.
                """
                app_templates_cache[template_id] = ''
                app_template_output = ''
        else:
            app_template_output = app_templates_cache[template_id]

        result.append(app_template_output)

    return mark_safe(' '.join(result))


@register.filter
def appearance_get_choice_value(field):
    try:
        return dict(field.field.choices)[field.value()]
    except TypeError:
        return ', '.join([subwidget.data['label'] for subwidget in field.subwidgets if subwidget.data['selected']])
    except KeyError:
        return _('None')

## Add Theme Script ##
@register.simple_tag
def appearance_get_user_theme_script():
    try:
        obj = Theme.objects.get(id=1)
        context = obj.logo +  "|" + obj.stylesheet + "|" + obj.navbarcolor + "|" + obj.menucolor
    except Theme.DoesNotExist:
        context = "Mayan-EDMS||#ffffff|#2f3c4f|#2f3c4f|#2f3c4f|#ffffff|#2f3c4f|#1b232e|#fe0000|#4aaa97|#95a5a6|19|15|50|#ffffff"    
    
    return context


@register.simple_tag
def color_background_nav():
    try:
        obj = Theme.objects.get(id=1)
        context = obj.navbarcolor
    except Theme.DoesNotExist:
        return '#2f3c4f'
    return context

@register.filter
def appearance_get_form_media_js(form):
    return [form.media.absolute_path(path) for path in form.media._js]


@register.simple_tag
def appearance_get_icon(icon_path):
    return import_string(dotted_path=icon_path).render()

import time
@register.simple_tag
def appearance_get_user_theme_stylesheet(user):
    print(f'\n\nappearance_get_user_theme_stylesheet : { time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) }\n\n') # TODO: Chonsawat Logo Doing
    User = get_user_model()

    if user and user.is_authenticated:
        try:
            theme = user.theme_settings.theme
        except User.theme_settings.RelatedObjectDoesNotExist:
            # User had a setting assigned which was later deleted.
            return ''
        else:
            print("Chonsawat notify at: apps/apperance/templatetags/appearance_tag.py --method appearance_get_user_theme_stylesheet")
            if theme:
                print(f"{user.theme_settings.theme.logo}")
                return user.theme_settings.theme.stylesheet

    return ''


@register.simple_tag
def appearance_icon_render(icon, enable_shadow=False):
    return icon.render(extra_context={'enable_shadow': enable_shadow})


@register.filter
def appearance_object_list_count(object_list):
    try:
        return object_list.count()
    except TypeError:
        return len(object_list)

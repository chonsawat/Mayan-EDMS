# Generated by Django 2.2.24 on 2022-03-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0004_theme_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='menucolor',
            field=models.CharField(blank=True, help_text='Choose a color to change the Menu.', max_length=128, verbose_name='Menu Color'),
        ),
        migrations.AddField(
            model_name='theme',
            name='navbarcolor',
            field=models.CharField(blank=True, help_text='Choose a color to change the navbar.', max_length=128, verbose_name='Navbar Color'),
        ),
    ]

# Generated by Django 2.2.24 on 2022-03-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0003_auto_20210823_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='logo',
            field=models.TextField(blank=True, default='https://lh3.googleusercontent.com/fife/AAWUweULhkCLGFq9L8BUSFYnuWiRPhSp-dpqSnrRy3SlPKxp8u3Uiq_r_4otrCDMwaedmJZWi-9wgbTMtjQftF_n52djRhB84Ccosq93jAbSM4krlnVY4RxFUV02tsHSEjDy9pEcR8pyujKvJ47iwN_-Cn9h6f3jx7vhBXJY9pNtsss6uuuwjGitbGJbuka85LOhfmsLUPl_nWueZjo38mbtn2zFcBoGm-1-cqRQKClc6EzuhCSfK8R2Z17w969ix7f6dPQz7zNLlICtQa-yVTM_1Q-n7pYRDjSeKLsLybHKHSBOHi3755-uOQiA7wnj-_QCmVcSMYuWIid0Ih22AO8fUDtcLndssboU-Ne41XyY9v8mp0egQ4wYEn6QphN-9OR0m0mbf8yYSJpQ62ysiVPvsG671s25mlgnoiFmXeP2h2HLfPO2jVO4cYhzD1nV1Fvm5ACAJp9i0GVvuigDO4CB0sA20traVLs4R8oI9U5mwp48xsZYGz02Ib6whyKqZ8Bzb0K5T3su-bcE_OpCj4EpiJaG9O6A6syElXLCQPno_4RR9nijcEgtH2OVmz2a3SauETpOYnjbe3PisK8RnZBK7HIaB9k-LM8JrxEVBvvKG5Y7lFIsxkmg-JXlLFLCBzbSt_ys07Nari9AdCjSrBRVBgwy5X1cdqIAIHjSM1iJi1gZOJP6yLi6z6K5fp3Za86-DTJWnJR9PWvSUoyoijv5kfsHzF5f8ZVdWw=w1920-h955', help_text='The url to change your logo.', verbose_name='Logo'),
        ),
    ]

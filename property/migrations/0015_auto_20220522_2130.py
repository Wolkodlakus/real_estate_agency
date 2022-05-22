# Generated by Django 2.2.24 on 2022-05-22 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220522_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='text_complain',
            field=models.TextField(blank=True, default='', verbose_name='Текст жалобы:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
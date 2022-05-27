# Generated by Django 2.2.24 on 2022-05-22 18:05

from django.db import migrations


def replace_none(apps, schema_editor):
    """
    Замена None на ''
    """
    Complain = apps.get_model('property', 'Complain')
    for complain in Complain.objects.all().filter(text_complain__isnull=True):
        complain.text_complain = ''
        complain.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220522_2047'),
    ]

    operations = [
        migrations.RunPython(replace_none),
    ]

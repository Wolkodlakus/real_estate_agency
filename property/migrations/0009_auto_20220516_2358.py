# Generated by Django 2.2.24 on 2022-05-16 20:58
import phonenumbers
from django.db import migrations

def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            phonenumber_parse = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if not phonenumbers.is_valid_number(phonenumber_parse):
                flat.owner_pure_phone = None
                flat.save()
                continue
        except phonenumbers.phonenumberutil.NumberParseException:
            flat.owner_pure_phone = None
            flat.save()
            continue
        flat.owner_pure_phone = phonenumbers.format_number(
            phonenumber_parse,
            phonenumbers.PhoneNumberFormat.E164)
        flat.save()

    pass

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber),
    ]

# Generated by Django 2.2.24 on 2022-03-24 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220323_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сomplain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat')),
            ],
        ),
    ]

# Generated by Django 3.1.14 on 2022-06-30 09:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_otn_allow_big_solidus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedmessage',
            name='embeds',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, help_text='Embeds attached to this message.', size=None),
        ),
    ]
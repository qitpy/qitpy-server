# Generated by Django 4.1.3 on 2022-11-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_portfolioaccessfrequency_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomessage',
            name='name_or_email',
            field=models.TextField(blank=True, null=True),
        ),
    ]
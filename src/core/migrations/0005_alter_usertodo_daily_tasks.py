# Generated by Django 4.1.3 on 2022-11-24 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_portfoliomessage_name_or_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertodo',
            name='daily_tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily', to='core.todocard'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-24 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_usertodo_daily_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todocard',
            name='user_todo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.usertodo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomonth',
            name='user_todo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.usertodo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoschedule',
            name='user_todo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.usertodo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoyear',
            name='user_todo',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='core.usertodo'),
            preserve_default=False,
        ),
    ]
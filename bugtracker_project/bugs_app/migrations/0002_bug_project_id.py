# Generated by Django 3.0.8 on 2020-07-14 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
        ('bugs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='project_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='projects_app.Project'),
        ),
    ]

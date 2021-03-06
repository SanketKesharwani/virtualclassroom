# Generated by Django 3.0 on 2021-11-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_attendence_studentattendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccineRequired', models.IntegerField(blank=True, default=0, null=True)),
                ('classStrength', models.IntegerField(blank=True, default=0, null=True)),
                ('studentList', models.TextField(blank=True, null=True)),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ClassRoom')),
            ],
        ),
    ]

# Generated by Django 3.0 on 2021-11-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_studentdetails_studentdepartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='academicYear',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='facultydetails',
            name='experience',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='offlineclass',
            name='offlineStatus',
            field=models.CharField(blank=True, default='NO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='yearOfStudy',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
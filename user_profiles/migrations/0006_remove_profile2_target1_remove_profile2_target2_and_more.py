# Generated by Django 4.1.5 on 2023-03-04 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0005_alter_profile2_subject3_alter_profile2_subject4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile2',
            name='target1',
        ),
        migrations.RemoveField(
            model_name='profile2',
            name='target2',
        ),
        migrations.RemoveField(
            model_name='profile2',
            name='target3',
        ),
        migrations.RemoveField(
            model_name='profile2',
            name='target4',
        ),
    ]

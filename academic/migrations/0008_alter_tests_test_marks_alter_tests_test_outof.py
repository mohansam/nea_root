# Generated by Django 4.1.5 on 2023-03-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_rename_resources_topics_resource_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='test_marks',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tests',
            name='test_outof',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]

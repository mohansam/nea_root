# Generated by Django 4.1.5 on 2023-01-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_tests_test_given_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tests',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='month',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='year',
        ),
        migrations.AlterField(
            model_name='tests',
            name='test_subject',
            field=models.CharField(choices=[('Economics', 'Economics'), ('Art', 'Art'), ('English', 'English'), ('Maths', 'Maths'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Politics', 'Politics'), ('History', 'History'), ('Geography', 'Geography'), ('Psychology', 'Psychology'), ('Further Maths', 'Further Maths'), ('Spanish', 'Spanish'), ('Physical Education', 'Physical Education')], max_length=20),
        ),
    ]
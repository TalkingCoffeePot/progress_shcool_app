# Generated by Django 5.0.2 on 2024-03-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_tests', '0005_usertest_attempts_usertest_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetest',
            name='countdown',
            field=models.DurationField(blank=True, default=None, null=True),
        ),
    ]
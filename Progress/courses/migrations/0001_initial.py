# Generated by Django 5.0.2 on 2024-02-21 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('date_start', models.DateField()),
                ('date_finish', models.DateField()),
                ('paid_by', models.ManyToManyField(blank=True, limit_choices_to={'role': 'user'}, related_name='paid_courses', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, limit_choices_to={'role': 'user'}, related_name='enrolled_courses', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ManyToManyField(limit_choices_to={'role': 'teacher'}, related_name='courses_taught', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=255)),
                ('grade', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=5000)),
                ('video', models.URLField(null=True)),
                ('datetime', models.DateTimeField()),
                ('lesson_type', models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], default='free', max_length=4)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_currently_viewing', models.BooleanField()),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='courses.lesson')),
                ('students', models.ForeignKey(blank=True, limit_choices_to={'role', 'user'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

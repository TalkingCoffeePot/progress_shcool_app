# Generated by Django 5.0.2 on 2024-03-01 16:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_course_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курсы', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Урок'},
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Посещения', 'verbose_name_plural': 'Посещения'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='courses.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], default=('free', 'Free'), max_length=4, verbose_name='Бесплатный/платный'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='students',
            field=models.ForeignKey(blank=True, limit_choices_to={'role', 'user'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visits', to=settings.AUTH_USER_MODEL),
        ),
    ]
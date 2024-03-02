# Generated by Django 5.0.2 on 2024-02-29 18:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(limit_choices_to={'role': 'user'}, on_delete=django.db.models.deletion.CASCADE, related_name='comments_received', to=settings.AUTH_USER_MODEL, verbose_name='Ученик'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, related_name='comments_given', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='...', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('user', 'User')], max_length=30, verbose_name='Должность'),
        ),
    ]
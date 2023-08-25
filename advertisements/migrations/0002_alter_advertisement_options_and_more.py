# Generated by Django 4.2.4 on 2023-08-29 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'), ('CLOSED', 'Закрыто')], default='OPEN', verbose_name='Опубликованное'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]

# Generated by Django 3.2.19 on 2023-08-28 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230827_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите достижение', max_length=255, verbose_name='Достижение')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение', upload_to='users/achievements/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание достижения')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.achievement', verbose_name='Достижение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_achievement', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Достижение пользователя',
                'verbose_name_plural': 'Достижения пользователя',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='achievements',
            field=models.ManyToManyField(through='users.UserAchievement', to='users.Achievement'),
        ),
        migrations.AddConstraint(
            model_name='userachievement',
            constraint=models.UniqueConstraint(fields=('user', 'achievement'), name='unique achievement for user'),
        ),
    ]

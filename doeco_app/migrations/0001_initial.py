# Generated by Django 4.1 on 2022-08-15 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='simple one-line text.', max_length=100, verbose_name='DESCRIPTION')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/', verbose_name='IMAGE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('like', models.PositiveSmallIntegerField(default=0, verbose_name='LIKE')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doeco_app.category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('update_dt',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='UPDATE DT')),
                ('like', models.PositiveSmallIntegerField(default=0, verbose_name='LIKE')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doeco_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Ecospot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(default='', max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        )

    ]

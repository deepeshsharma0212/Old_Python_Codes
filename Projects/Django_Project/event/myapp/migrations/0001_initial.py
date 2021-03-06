# Generated by Django 2.0 on 2017-12-17 17:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_pics/', verbose_name='Profile Picture')),
                ('birth_day', models.DateField()),
                ('Bio', models.TextField()),
                ('user', models.ForeignKey(on_delete='CASECADE', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]

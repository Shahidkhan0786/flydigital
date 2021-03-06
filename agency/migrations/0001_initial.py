# Generated by Django 3.2.3 on 2021-05-26 12:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)])),
                ('city', models.CharField(default='', max_length=250, null=True)),
                ('zipcode', models.CharField(max_length=250, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('widow', 'widow'), ('seprated', 'seprated'), ('commited', 'commited')], default='single', max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('pic', models.ImageField(null=True, upload_to='uploads/product/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

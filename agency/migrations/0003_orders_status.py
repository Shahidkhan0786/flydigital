# Generated by Django 3.2.3 on 2021-05-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('accept', 'accept'), ('Indevelop', 'Indevelop'), ('completed', 'completed'), ('delivered', 'delivered')], default='Pending', max_length=200),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stays', '0007_auto_20200430_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='check_in',
            field=models.CharField(choices=[('Lockbox', 'Lockbox'), ('Smartlock', 'Smartlock'), ('Keypad', 'Keypad')], default='Lockbox', max_length=30),
        ),
    ]

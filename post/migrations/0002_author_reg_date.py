# Generated by Django 4.0.1 on 2022-02-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='reg_date',
            field=models.DateField(auto_now_add=True, default='2015-01-27'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Draft'),
        ),
    ]
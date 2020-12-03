# Generated by Django 3.1.2 on 2020-11-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201113_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', related_query_name='comment_like', to='blog.comment', verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='postsetting',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_setting', related_query_name='post_setting', to='blog.post', verbose_name='Post'),
        ),
    ]

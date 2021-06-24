# Generated by Django 3.1.2 on 2021-06-24 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(default='code', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default='python', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
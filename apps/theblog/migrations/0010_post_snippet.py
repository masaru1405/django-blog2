# Generated by Django 4.0.5 on 2022-08-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog post...', max_length=255),
        ),
    ]

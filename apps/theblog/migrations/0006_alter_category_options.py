# Generated by Django 4.0.5 on 2022-08-06 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

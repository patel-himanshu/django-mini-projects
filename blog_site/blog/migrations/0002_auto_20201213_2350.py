# Generated by Django 3.1.3 on 2020-12-13 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='blog_post_tables',
        ),
    ]
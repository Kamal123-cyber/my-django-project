# Generated by Django 3.1 on 2022-10-29 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
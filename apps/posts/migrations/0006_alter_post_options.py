# Generated by Django 3.2.6 on 2021-08-18 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
    ]

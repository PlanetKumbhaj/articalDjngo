# Generated by Django 4.1.1 on 2022-09-17 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
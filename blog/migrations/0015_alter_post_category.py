# Generated by Django 4.1.1 on 2022-09-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Technology', 'Technology'), ('Travel', 'Travel'), ('Entertainment', 'Entertainment'), ('Gaming', 'Gaming'), ('Health & Fitness', 'Health & Fitness'), ('Political', 'Political'), ('Education', 'Education'), ('Fashion', 'Fashion'), ('General', 'General')], default='college', max_length=50),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_post_mod_warning'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
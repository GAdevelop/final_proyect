# Generated by Django 4.0.5 on 2022-06-27 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_costumuser_profile_pic_costumuser_second_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPosts', '0002_auto_20210329_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
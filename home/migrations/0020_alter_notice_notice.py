# Generated by Django 4.0.2 on 2022-03-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_notice_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice',
            field=models.TextField(max_length=100),
        ),
    ]

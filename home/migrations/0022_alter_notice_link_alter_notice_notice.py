# Generated by Django 4.0.2 on 2022-03-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_notice_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice',
            field=models.TextField(),
        ),
    ]

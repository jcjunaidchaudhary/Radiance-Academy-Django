# Generated by Django 3.2.5 on 2022-01-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
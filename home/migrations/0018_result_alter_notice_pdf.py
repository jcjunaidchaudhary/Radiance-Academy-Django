# Generated by Django 4.0.2 on 2022-03-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_notice_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='Result/images')),
            ],
        ),
        migrations.AlterField(
            model_name='notice',
            name='pdf',
            field=models.FileField(default='Not Available', upload_to='Notice/pdf'),
        ),
    ]
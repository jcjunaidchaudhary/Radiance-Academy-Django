# Generated by Django 3.2.5 on 2022-01-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pdf', models.FileField(default='', upload_to='Question pepar/pdf')),
                ('date', models.DateField()),
            ],
        ),
    ]

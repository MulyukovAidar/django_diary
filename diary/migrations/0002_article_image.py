# Generated by Django 2.1.1 on 2018-09-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(null=True, upload_to='article_attachments'),
        ),
    ]

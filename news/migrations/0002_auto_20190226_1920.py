# Generated by Django 2.1.7 on 2019-02-26 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
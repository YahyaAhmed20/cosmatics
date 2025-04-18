# Generated by Django 5.1.7 on 2025-04-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_slide_description_ar_slide_description_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'Slide', 'verbose_name_plural': 'Slides'},
        ),
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='description_ar',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='description_he',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='slider_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle',
            field=models.CharField(max_length=255, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle_ar',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle_he',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_ar',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_he',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]

# Generated by Django 2.0 on 2021-07-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_remove_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='books_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='original_publication_year',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='small_image_url',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
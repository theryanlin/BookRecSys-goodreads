# Generated by Django 2.0 on 2021-07-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_auto_20210716_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
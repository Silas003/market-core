# Generated by Django 4.2.2 on 2023-10-14 21:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_remove_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='items'),
            preserve_default=False,
        ),
    ]

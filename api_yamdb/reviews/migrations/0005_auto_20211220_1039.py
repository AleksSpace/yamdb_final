# Generated by Django 2.2.16 on 2021-12-20 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20211220_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genretitle',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='genretitle',
            old_name='title_id',
            new_name='title',
        ),
    ]

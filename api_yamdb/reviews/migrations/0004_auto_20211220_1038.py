# Generated by Django 2.2.16 on 2021-12-20 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_title_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre_title',
            new_name='GenreTitle',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['slug'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['slug'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='genretitle',
            options={'verbose_name': 'Жанр произведения', 'verbose_name_plural': 'Жанры произведений'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]

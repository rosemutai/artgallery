# Generated by Django 2.2 on 2020-06-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'verbose_name_plural': 'Art'},
        ),
        migrations.AlterModelOptions(
            name='artcategory',
            options={'verbose_name_plural': 'ArtCategories'},
        ),
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(upload_to='myimages'),
        ),
    ]

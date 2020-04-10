# Generated by Django 2.2.12 on 2020-04-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(),
        ),
    ]
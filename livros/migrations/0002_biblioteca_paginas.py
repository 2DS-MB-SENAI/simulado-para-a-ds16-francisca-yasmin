# Generated by Django 4.2 on 2025-04-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblioteca',
            name='paginas',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]

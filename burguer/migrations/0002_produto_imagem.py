# Generated by Django 4.2.4 on 2023-08-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]

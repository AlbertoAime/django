# Generated by Django 2.1.2 on 2019-06-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha de publicación')),
            ],
        ),
    ]

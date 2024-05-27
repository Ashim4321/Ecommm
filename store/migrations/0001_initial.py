# Generated by Django 5.0.4 on 2024-04-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='files/')),
            ],
        ),
    ]

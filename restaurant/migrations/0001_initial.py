# Generated by Django 4.0.4 on 2022-06-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/restaurants')),
                ('kitchen_style', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
            ],
        ),
    ]

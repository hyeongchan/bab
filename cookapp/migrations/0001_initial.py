# Generated by Django 2.2.4 on 2019-08-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=10, null=True)),
                ('category', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('url', models.URLField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('ingredients', models.ManyToManyField(to='cookapp.Post')),
            ],
        ),
    ]

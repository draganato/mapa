# Generated by Django 3.1.2 on 2020-11-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podaci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uslov', models.BooleanField(null=True)),
                ('tacka', models.CharField(max_length=200, null=True)),
                ('poligon', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=100)),
                ('y', models.CharField(max_length=100)),
                ('Unique_Squirrel_ID', models.CharField(max_length=100)),
                ('Shift', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
    ]

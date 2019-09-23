# Generated by Django 2.2.5 on 2019-09-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Title of Card', max_length=50)),
                ('desc', models.TextField(help_text='Description')),
            ],
        ),
    ]

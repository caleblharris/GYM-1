# Generated by Django 3.1.1 on 2021-04-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210418_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email_name', models.TextField()),
                ('phone_number', models.IntegerField()),
                ('address_number', models.IntegerField()),
                ('address_name', models.TextField()),
                ('password_name', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Person',
            new_name='Customer',
        ),
    ]

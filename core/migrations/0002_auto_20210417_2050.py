# Generated by Django 3.1.1 on 2021-04-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id_name', models.TextField()),
                ('check_in_date', models.IntegerField()),
                ('check_in_time', models.IntegerField()),
                ('check_out_time', models.IntegerField()),
                ('instructor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id_name', models.IntegerField()),
                ('status_name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='person',
        ),
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.RemoveField(
            model_name='person',
            name='courses',
        ),
        migrations.AddField(
            model_name='person',
            name='address_name',
            field=models.TextField(default=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='address_number',
            field=models.IntegerField(default=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='instructor',
            field=models.TextField(default=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='person_id_name',
            field=models.IntegerField(default=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(default=140),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]

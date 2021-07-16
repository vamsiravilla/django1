# Generated by Django 3.2.5 on 2021-07-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=200)),
                ('empmobileno', models.IntegerField(max_length=13)),
                ('empaddress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('HRid', models.IntegerField(primary_key=True, serialize=False)),
                ('HRname', models.CharField(max_length=200)),
                ('HRmobileno', models.IntegerField(max_length=13)),
                ('HRaddress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=200)),
                ('stumobileno', models.IntegerField(max_length=13)),
                ('stuaddress', models.TextField()),
            ],
        ),
    ]
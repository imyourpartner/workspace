# Generated by Django 3.1.2 on 2020-11-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOne', models.CharField(max_length=20)),
                ('nameTwo', models.CharField(max_length=20)),
                ('nameThere', models.CharField(max_length=20)),
                ('surnameOne', models.CharField(max_length=20)),
                ('surnameTwo', models.CharField(max_length=20)),
                ('surnameThere', models.CharField(max_length=20)),
            ],
        ),
    ]

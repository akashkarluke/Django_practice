# Generated by Django 3.2.7 on 2021-10-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_no', models.IntegerField()),
                ('f_name', models.CharField(max_length=30)),
                ('f_sal', models.FloatField()),
                ('f_city', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
    ]

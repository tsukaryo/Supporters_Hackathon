# Generated by Django 3.1 on 2022-06-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESMaker', '0004_auto_20220618_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('company_id', models.IntegerField()),
                ('question_id', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBoard',
            fields=[
                # Primary Key 따로 만들어주지 않으면 Django가 자동적으로 id 만들어줌
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mytitle', models.CharField(max_length=500)),
                ('mycontent', models.CharField(max_length=2000)),
                ('mydate', models.DateTimeField()),
            ],
        ),
    ]
# Generated by Django 3.2.10 on 2021-12-17 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railapp', '0004_auto_20211215_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['created_on']},
        ),
    ]

# Generated by Django 3.1.7 on 2022-04-10 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('khottab', '0010_auto_20220411_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imam',
            options={'ordering': ['nationality'], 'permissions': (('can_view', 'view'),)},
        ),
    ]

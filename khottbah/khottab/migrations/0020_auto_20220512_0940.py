# Generated by Django 3.1.7 on 2022-05-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khottab', '0019_auto_20220512_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imam',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

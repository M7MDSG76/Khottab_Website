# Generated by Django 3.1.7 on 2022-03-30 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('khottab', '0006_auto_20220330_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khottbah',
            name='imam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='khottab.imam'),
        ),
    ]

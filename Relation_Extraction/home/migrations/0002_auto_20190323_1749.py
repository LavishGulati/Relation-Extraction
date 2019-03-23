# Generated by Django 2.1.5 on 2019-03-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='object_1_type',
            field=models.CharField(default='dsjakoj', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='object_2_type',
            field=models.CharField(default='dnsaji', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='object',
            name='object_1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='object',
            name='object_2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='object',
            name='relation',
            field=models.CharField(max_length=500),
        ),
    ]
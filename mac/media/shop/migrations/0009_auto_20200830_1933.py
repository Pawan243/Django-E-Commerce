# Generated by Django 3.0.4 on 2020-08-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200723_0816'),
    ]

    operations = [
        migrations.DeleteModel(
            name='register',
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]

# Generated by Django 2.2 on 2020-01-10 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20200110_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Member'),
        ),
    ]

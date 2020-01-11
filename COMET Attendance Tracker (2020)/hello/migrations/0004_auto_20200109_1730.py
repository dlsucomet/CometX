# Generated by Django 2.2.4 on 2020-01-09 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200109_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='uid',
            new_name='member',
        ),
        migrations.AlterField(
            model_name='log',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Member'),
        ),
    ]
# Generated by Django 2.2.4 on 2020-01-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_auto_20200111_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='residencylog',
            old_name='minutes',
            new_name='seconds',
        ),
        migrations.AlterField(
            model_name='log',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Member'),
        ),
        migrations.AlterField(
            model_name='residencylog',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Member'),
        ),
    ]

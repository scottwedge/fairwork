# Generated by Django 2.0.4 on 2018-05-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditor', '0015_auto_20180512_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requester',
            name='aws_account',
        ),
        migrations.AddField(
            model_name='requester',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
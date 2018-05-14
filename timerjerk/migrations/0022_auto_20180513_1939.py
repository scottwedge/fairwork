# Generated by Django 2.0.4 on 2018-05-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timerjerk', '0021_hittype_requester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requester',
            name='aws_account',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='requester',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
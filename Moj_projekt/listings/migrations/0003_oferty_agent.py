# Generated by Django 2.1.1 on 2019-04-30 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20190430_1612'),
        ('listings', '0002_auto_20190430_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferty',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Agenci'),
        ),
    ]

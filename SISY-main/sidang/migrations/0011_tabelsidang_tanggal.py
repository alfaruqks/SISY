# Generated by Django 4.2.1 on 2023-06-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidang', '0010_delete_tabelwaktusidang'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabelsidang',
            name='tanggal',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]
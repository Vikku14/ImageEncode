# Generated by Django 3.0.7 on 2020-06-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encode', '0006_auto_20200615_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='base64_format',
            field=models.TextField(),
        ),
    ]

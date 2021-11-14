# Generated by Django 3.2.9 on 2021-11-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_externaluser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externaluser',
            name='email',
            field=models.EmailField(blank=True, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='externaluser',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='externaluser',
            name='public_id',
            field=models.UUIDField(blank=True, editable=False),
        ),
    ]
# Generated by Django 4.2.5 on 2024-02-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_alter_dignities_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Активный?'),
        ),
    ]
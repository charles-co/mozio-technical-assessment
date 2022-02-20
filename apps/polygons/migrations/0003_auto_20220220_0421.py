# Generated by Django 3.2.12 on 2022-02-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygons', '0002_polygon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polygon',
            options={'ordering': ['price']},
        ),
        migrations.AddConstraint(
            model_name='polygon',
            constraint=models.UniqueConstraint(fields=('provider', 'poly'), name='unique_polygon'),
        ),
    ]
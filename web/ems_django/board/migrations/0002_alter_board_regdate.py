# Generated by Django 4.2.3 on 2023-07-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="regdate",
            field=models.DateTimeField(null=True),
        ),
    ]

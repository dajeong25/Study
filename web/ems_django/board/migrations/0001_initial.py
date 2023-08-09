# Generated by Django 4.2.3 on 2023-07-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("pw", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=200)),
                ("content", models.CharField(max_length=2000)),
                ("regdate", models.DateField(null=True)),
                ("readcnt", models.IntegerField(default=0)),
                ("file1", models.CharField(max_length=300)),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgeting", "0006_category_alter_budgetentry_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budgetentry",
            name="category",
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-05 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgeting", "0005_remove_budget_amount_remove_budget_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "budget",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="budgeting.budget",
                    ),
                ),
            ],
            options={"db_table": "CATEGORY",},
        ),
        migrations.AlterField(
            model_name="budgetentry",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="budgeting.category"
            ),
        ),
    ]

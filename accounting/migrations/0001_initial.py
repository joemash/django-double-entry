# Generated by Django 5.1.2 on 2024-10-24 10:56

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountHeading",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.IntegerField(blank=True, null=True)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_by", models.IntegerField(blank=True, null=True)),
                ("heading", models.CharField(max_length=255)),
                (
                    "heading_type",
                    models.CharField(
                        choices=[
                            ("asset", "Asset"),
                            ("liability", "Liability"),
                            ("revenue", "Revenue"),
                            ("expense", "Expense"),
                            ("equity", "Equity"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "balance_type",
                    models.CharField(
                        choices=[("dr", "DR"), ("cr", "CR")], max_length=255
                    ),
                ),
                ("number", models.IntegerField()),
                ("tracker", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("-updated", "-created"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AccountingTransaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.IntegerField(blank=True, null=True)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_by", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField()),
            ],
            options={
                "ordering": ("-updated", "-created"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.IntegerField(blank=True, null=True)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_by", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=50, unique=True)),
                ("code", models.CharField(max_length=5, unique=True)),
                ("is_default", models.BooleanField(default=False)),
                (
                    "conversion_rate",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=15, null=True
                    ),
                ),
            ],
            options={
                "ordering": ("-updated", "-created"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.IntegerField(blank=True, null=True)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_by", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("is_control_account", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("number", models.CharField(blank=True, max_length=255)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="accounting.account",
                    ),
                ),
                (
                    "heading",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="child_accounts",
                        to="accounting.accountheading",
                    ),
                ),
            ],
            options={
                "ordering": ("-updated", "-created"),
            },
        ),
        migrations.CreateModel(
            name="AccountingEntry",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.IntegerField(blank=True, null=True)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_by", models.IntegerField(blank=True, null=True)),
                (
                    "dr_amount",
                    models.DecimalField(decimal_places=4, default=0, max_digits=16),
                ),
                (
                    "cr_amount",
                    models.DecimalField(decimal_places=4, default=0, max_digits=16),
                ),
                (
                    "entry_date",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="account_entries",
                        to="accounting.account",
                    ),
                ),
                (
                    "transaction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="transaction_account_entries",
                        to="accounting.accountingtransaction",
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="currency",
                        to="accounting.currency",
                    ),
                ),
            ],
            options={
                "ordering": ("-updated", "-created"),
                "abstract": False,
            },
        ),
    ]

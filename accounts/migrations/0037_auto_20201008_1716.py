# Generated by Django 2.1.3 on 2020-10-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0036_auto_20201008_1613"),
    ]

    operations = [
        migrations.RenameField(
            model_name="discount", old_name="promo", new_name="promo_text",
        ),
        migrations.AlterField(
            model_name="subscription",
            name="plan",
            field=models.CharField(
                choices=[
                    ("plan_GwSV9PWY04hZ93", "Tiered pricing"),
                    ("plan_Ek0Ns9AhiBtR1o", "Early Adopter - $20/user per month"),
                    ("plan_GgYpcKU6ncOBVe", "Small - $49/user per month"),
                    ("plan_Gh1Ya0ebnwkY54", "Medium - $99/user per month"),
                    ("price_1GxXnOCZ3jbVsfoGC0N3fx5e", "Free for 1 user"),
                    ("price_1GxXnPCZ3jbVsfoGVEbjyVik", "SMB - $25/m for up to 3 users"),
                    (
                        "price_1GxXnPCZ3jbVsfoGz6P2AXi0",
                        "Growth - $49/m for unlimited users",
                    ),
                    (
                        "price_1Ha1i2CZ3jbVsfoGUPC3cRB5",
                        "AppSumo - $99 for for lifetime access",
                    ),
                ],
                max_length=255,
            ),
        ),
    ]

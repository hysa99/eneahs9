# Generated by Django 4.1.7 on 2023-04-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0010_remove_blogs_items_likes_blogs_items_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="color",
            field=models.CharField(
                choices=[
                    ("bg-yellow-500", "bg-yellow-500"),
                    ("bg-pink-500", "bg-pink-500"),
                    ("bg-orange-500", "bg-orange-500"),
                    ("bg-blue-500", "bg-blue-500"),
                    ("bg-green-500", "bg-green-500"),
                    ("bg-red-500", "bg-red-500"),
                    ("b-purple-500", "bg-purple-500"),
                ],
                default="bg-orange-500",
                max_length=50,
            ),
        ),
    ]

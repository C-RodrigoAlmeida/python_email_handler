# Generated by Django 4.2.12 on 2024-08-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inbox", "0005_rename_message_messagetemplate_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="recipients",
            field=models.ManyToManyField(
                related_name="group_recipients", to="inbox.recipient"
            ),
        ),
    ]

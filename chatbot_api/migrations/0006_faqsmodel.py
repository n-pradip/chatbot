# Generated by Django 5.0.2 on 2024-03-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_api', '0005_rename_dashboardiamge_dashboardimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]

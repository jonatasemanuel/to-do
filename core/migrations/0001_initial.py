# Generated by Django 4.1.5 on 2023-01-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=80, verbose_name='To- do...')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

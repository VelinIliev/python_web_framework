# Generated by Django 4.2.1 on 2023-06-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tools', '0003_alter_employees_age_alter_employees_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageViewTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, null=True)),
                ('last_name', models.CharField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
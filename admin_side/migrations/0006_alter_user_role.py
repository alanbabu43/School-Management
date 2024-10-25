# Generated by Django 5.1.2 on 2024-10-23 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('staff', 'Staff'), ('librarian', 'Librarian')], max_length=10),
        ),
    ]
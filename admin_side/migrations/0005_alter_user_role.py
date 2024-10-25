# Generated by Django 5.1.2 on 2024-10-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0004_alter_books_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student'), ('Staff', 'Staff'), ('Librarian', 'Librarian')], max_length=10),
        ),
    ]
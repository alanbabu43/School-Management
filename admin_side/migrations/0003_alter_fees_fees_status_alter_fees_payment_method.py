# Generated by Django 5.1.2 on 2024-10-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0002_alter_fees_fees_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='fees_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Partially Paid', 'Partially Paid')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fees',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer'), ('Online Payment', 'Online Payment')], max_length=20, null=True),
        ),
    ]
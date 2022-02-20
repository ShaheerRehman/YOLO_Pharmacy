# Generated by Django 4.0.2 on 2022-02-20 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('license_no', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('salt_name', models.CharField(max_length=256)),
                ('salt_quantity', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('mg', 'Mg'), ('mcg', 'Mcg')], max_length=128, null=True)),
                ('buying_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('shelf_number', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('pack_quantity', models.CharField(max_length=128)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='yolo_site.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('job_title', models.CharField(blank=True, max_length=128)),
                ('contact_no', models.CharField(blank=True, max_length=128)),
                ('bank_account', models.CharField(blank=True, max_length=256)),
                ('salary', models.FloatField(blank=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=128)),
                ('quantity', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('generated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='detail_billing_employee', to=settings.AUTH_USER_MODEL)),
                ('med_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billed_med', to='yolo_site.medicine')),
            ],
        ),
    ]

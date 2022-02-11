from django.db import models
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    license_no = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    added_on = models.DatetimeField(auto_now_add=True)

class MedDetails(models.Model):
    class Type(models.TextChoices):
        mg = "milligrams"
        mcg = "micrograms"
    salt_name = models.CharField(max_length=128)
    salt_quantity = models.FloatField()
    salt_quantity_type = models.CharField(max_length=128, choices=Type.choices, default=Type.mg, blank=True, null=True)
    added_on = models.DateTimeField(auto_now=True)

class Medicine(models.Model):
    pass
# last model to be created

class Customer(models.Model):
    name = models.CharField(max_length=128)
    contact_no = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    name = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)
    join_date = models.DateField(auto_now_add=True)
    contact_no = models.CharField(max_length=128)
    bank_acc = models.CharField(max_length=256)
    Salary = models.FloatField()
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class SalesReport(models.Model):
    customer_id = models.ForeignKey('yolo_site.Customer', related_name='billed_customer', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('yolo_site.Employee', related_name='billing_employee', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    total_revenue = models.FloatField()

class BillDetails(models.Model):
    customer_id = models.ForeignKey('yolo_site.Customer', related_name='billed_customer', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('yolo_site.Employee', related_name='billing_employee', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

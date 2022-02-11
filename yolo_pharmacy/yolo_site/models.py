from django.db import models
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    license_no = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class MedDetails(models.Model):
    class Type(models.TextChoices):
        mg = "milligrams"
        mcg = "micrograms"
    salt_name = models.CharField(max_length=128)
    salt_quantity = models.FloatField()
    salt_quantity_type = models.CharField(max_length=128, choices=Type.choices, default=Type.mg, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

class Medicine(models.Model):
    type = models.ForeignKey('yolo_site.MedDetails', related_name='med_details', on_delete=models.CASCADE)
    company = models.ForeignKey('yolo_site.Company', related_name='company', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    shelf_no = models.PositiveIntegerField()
    expiry = models.DateField()
    manufacturing = models.DateField()
    stock = models.PositiveIntegerField()
    pack_qty = models.CharField(max_length=128) #in the form of 3 X 10 for a pack of 3 strips containing 10 tabs each or 200 ml for liquids
    updated_on = models.DateField(auto_now=True)

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
    customer_id = models.ForeignKey('yolo_site.Customer', related_name='report_billed_customer', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('yolo_site.Employee', related_name='report_billing_employee', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    total_revenue = models.FloatField()

class BillDetails(models.Model):
    customer_id = models.ForeignKey('yolo_site.Customer', related_name='detail_billed_customer', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('yolo_site.Employee', related_name='detail_billing_employee', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

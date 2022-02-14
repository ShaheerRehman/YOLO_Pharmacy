from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    license_no = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('comp_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return self.name

class Medicine(models.Model):
    company = models.ForeignKey('yolo_site.Company', related_name='company', on_delete=models.CASCADE)
    class Type(models.TextChoices):
        mg = "mg"
        mcg = "mcg"
    name = models.CharField(max_length=128)
    salt_name = models.CharField(max_length=256)
    salt_quantity = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=128, choices=Type.choices, blank=True, null=True)
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    shelf_number = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    pack_quantity = models.CharField(max_length=128)
    # in the form of 10 X 3 for a pack of 3 strips containing 10 tabs each
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('med_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    name = models.CharField(max_length=128, blank=True)
    job_title = models.CharField(max_length=128, blank=True)
    contact_no = models.CharField(max_length=128, blank=True)
    bank_account = models.CharField(max_length=256, blank=True)
    salary = models.FloatField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('emp_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return self.user.username

class BillDetails(models.Model):
    employee_id = models.ForeignKey('yolo_site.Employee', related_name='detail_billing_employee', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=128),
    quantity = models.PositiveIntegerField()
    total_amount = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'To '+ str(self.customer_name) + ' From ' + self.employee_id.name

from django import forms
from . import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        exclude = ['added_on']

class MedDetailsForm(forms.ModelForm):
    class Meta:
        model = models.MedDetails
        exclude = ['added_on']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        exclude = ['updated_on']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        exclude = ['added_on']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        exclude = ['added_on']

class BillDetailsForm(forms.ModelForm):
    class Meta:
        model = models.BillDetails
        exclude = ['created_on']


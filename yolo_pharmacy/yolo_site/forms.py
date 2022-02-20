from django import forms
from django.contrib.auth.models import User
from . import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        exclude = ['added_on']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        exclude = ['updated_on']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['name', 'job_title', 'contact_no', 'bank_account', 'salary', 'address']

class BillDetailsForm(forms.ModelForm):
    class Meta:
        model = models.BillDetails
        exclude = ['created_on']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data['quantity']
        med_id = cleaned_data['med_id']
        if quantity > med_id.stock:
            self.add_error('quantity', 'Quantity exceeds stock')
        return cleaned_data
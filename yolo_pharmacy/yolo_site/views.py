
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from . import models
from . import forms
from django.views.generic import (View, TemplateView,
                                  CreateView, ListView,
                                  DetailView, DeleteView,
                                  UpdateView, )
# Create your views here

class IndexView(TemplateView):
    template_name = 'yolo_site/index.html'

class AboutView(TemplateView):
    template_name = 'yolo_site/about.html'

class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

class EmpListView(SuperUserCheck, ListView):
    model = models.Employee
    def get_queryset(self):
        return models.Employee.objects.filter(added_on__lte=timezone.now()).order_by('-added_on')

class EmpDetailView(SuperUserCheck, DetailView):
    model = models.Employee

class EmpUpdateView(SuperUserCheck, UpdateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    redirect_field_name = 'yolo_site/employee_detail.html'

class EmpDeleteView(SuperUserCheck, DeleteView):
    model = models.Employee
    success_url = reverse_lazy('emp_list')

@user_passes_test(lambda u: u.is_superuser)
def register(request):
    registered = False

    if request.method == "POST":

        user_form = forms.UserForm(data=request.POST)
        employee_form = forms.EmployeeForm(data=request.POST)

        if user_form.is_valid() and employee_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            registered = True
        else:
            print(user_form.errors, employee_form.errors)
    else:
        user_form = forms.UserForm()
        employee_form = forms.EmployeeForm()

    return render(request, 'yolo_site/employee_form.html',
                  {'user_form': user_form, 'employee_form': employee_form, 'registered': registered})

class CompCreateView(SuperUserCheck, CreateView):
    model = models.Company
    form_class = forms.CompanyForm
    redirect_field_name = 'yolo_site/company_detail.html'

class CompListView(SuperUserCheck, ListView):
    model = models.Company
    def get_queryset(self):
        return models.Company.objects.filter(added_on__lte=timezone.now()).order_by('-added_on')

class CompUpdateView(SuperUserCheck, UpdateView):
    model = models.Company
    # form_class = forms.CompanyForm
    fields = ['license_no', 'contact_no', 'address']
    redirect_field_name = 'yolo_site/company_detail.html'

class CompDetailView(SuperUserCheck, DetailView):
    model = models.Company


class CompDeleteView(SuperUserCheck, DeleteView):
    model = models.Company
    success_url = reverse_lazy('comp_list')

class MedCreateView(LoginRequiredMixin, CreateView):
    model = models.Medicine
    form_class = forms.MedicineForm
    redirect_field_name = 'yolo_site/medicine_detail.html'

class MedListView(LoginRequiredMixin, ListView):
    model = models.Medicine
    def get_queryset(self):
        return models.Medicine.objects.filter(updated_on__lte=timezone.now()).order_by('-updated_on')

class MedDetailView(LoginRequiredMixin, DetailView):
    model = models.Medicine

class MedUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Medicine
    fields = ['salt_quantity', 'unit', 'buying_price', 'selling_price', 'shelf_number', 'stock', 'pack_quantity']
    redirect_field_name = 'yolo_site/medicine_detail.html'

class MedDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Medicine
    success_url = reverse_lazy('med_list')


class BillCreateView(LoginRequiredMixin, CreateView):
    model = models.BillDetails
    form_class = forms.BillDetailsForm
    redirect_field_name = 'yolo_site/billdetails_detail.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.generated_by = self.request.user
        obj.save()
        obj.update_stock()

        obj.med_id.save()
        self.object = obj
        return HttpResponseRedirect(self.get_success_url())

class BillListView(LoginRequiredMixin, ListView):
    model = models.BillDetails
    def get_queryset(self):
        return models.BillDetails.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')

class BillDetailView(LoginRequiredMixin, DetailView):
    model = models.BillDetails

class BillDeleteView(LoginRequiredMixin, DeleteView):
    model = models.BillDetails
    success_url = reverse_lazy('bill_list')

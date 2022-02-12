from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from . import models
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import (View, TemplateView,
                                  CreateView, ListView,
                                  DetailView, DeleteView,
                                  UpdateView, )
from . import forms
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

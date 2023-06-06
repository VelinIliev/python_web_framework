from django import forms
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from temp_project.class_based_views.models import Employee


def index(request):
    return HttpResponse("index")


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': "CBV"
        }
        return render(request, 'cbv/cbv_index.html', context)

    def post(self, request):
        ...


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'cbv/cbv_index.html'
    extra_context = {"title": "Template view"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'cbv/cbv-list-view.html'
    extra_context = {"title": "List view"}

    # context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset \
                .filter(
                Q(first_name__icontains=pattern.lower()) |
                Q(last_name__icontains=pattern.lower()) |
                Q(seniority_level__icontains=pattern.lower())
            )

        queryset = queryset.order_by('seniority_level', 'first_name', 'last_name')
        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context


class EmployeeDetailsView(views.DetailView):
    model = Employee
    template_name = 'cbv/cbv-detail-view.html'
    extra_context = {"title": "Details view"}
    context_object_name = 'employee'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "First name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Last name"}),
        }


class EmployeeCreateView(views.CreateView):
    model = Employee
    template_name = 'cbv/cbv-create.html'
    fields = '__all__'

    # success_url = '/cbv/list/'
    # form_class = EmployeeCreateForm

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={'pk': created_object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        # for name, field in form.fields.items():
        #     field.widget.attrs['placeholder'] = f'Enter {name}'
        form.fields['first_name'].widget.attrs['placeholder'] = "First name"
        form.fields['last_name'].widget.attrs['placeholder'] = "Last name"
        return form


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    template_name = 'cbv/cbv-update.html'
    fields = '__all__'
    success_url = '/cbv/list/'


class EmployeeDeleteView(views.DeleteView):
    model = Employee
    template_name = 'cbv/cbv-delete.html'
    success_url = '/cbv/list/'

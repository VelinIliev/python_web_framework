import random
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from temp_project.web_tools.models import Employees, PageViewTest
from django.views import generic as views


def very_slow_operation():
    # sleep(2)
    return random.randint(1, 1024)


LATEST_VALUES_SESSION_KEY = 'LATEST_VALUES_SESSION_KEY'


# @cache_page(1 * 60)
def index(request):
    # Employees.objects.create(
    #     first_name="velin",
    #     last_name='iliev',
    #     age=25,
    # )
    value = very_slow_operation()

    latest_value = request.session.get(LATEST_VALUES_SESSION_KEY, [])
    latest_value = [value] + latest_value
    latest_value = latest_value[:3]
    request.session[LATEST_VALUES_SESSION_KEY] = latest_value

    return HttpResponse(f'value is: {value}, last 3 values: {", ".join(str(x) for x in latest_value)}')


CLICKS_COUNT_SESSION_KEY = 'CLICKS_COUNT_SESSION_KEY'


def clicks_counter(request):
    clicks_count = request.session.get(CLICKS_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICKS_COUNT_SESSION_KEY] = clicks_count
    return HttpResponse(f'clicks: {clicks_count}')


class EmployeesListViews(views.ListView):
    model = PageViewTest
    template_name = 'tools/list-view.html'
    default_paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)

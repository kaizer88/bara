from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import GenerateAdhocFileForm

import pathlib
import json

# Create your views here.

# @login_required()

import datetime


def workdays(d, end, exclude_weekends):
    days = []
    excluded = (6, 7)
    while d.date() <= end.date():
        if exclude_weekends is True:
            if d.isoweekday() not in excluded:
                days.append(d)
        d += datetime.timedelta(days=1)
    return days


print(workdays(datetime.datetime(2019, 1, 21),
               datetime.datetime(2019, 1, 30)))


def generate_file(request):
    if request.method == 'POST':
        portfolio_list = []
        export_sets = {}
        type_list = []
        date_ranges = []

        env = request.POST.get('env')
        types = request.POST.getlist('types')
        portfolios= request.POST.getlist('portfolios')
        stress_model = request.POST.get('stress_model')
        mcvar_model = request.POST.get('mcvar_model')
        headlines_model = request.POST.get('headlines_model')
        date_range = request.POST.get('date_range')
        ex_weekends = request.POST.get('ex_weekends')
        i = request.POST.get('ex_weekends')

        start_date = date_range[0:10]
        end_date = date_range[13:23]
        request.POST.getlist('types')

        for i in types:
            if "stress" in types:
                export_sets = {"types":i, "model":i}
                type_list.append(export_sets)

            if "mcvar" in types:
                export_sets = {"types":i, "model":i}
                type_list.append(export_sets)

            if "headlines" in types:
                export_sets = {"types":i, "model":i}
                type_list.append(export_sets)

            if "headline_assets" in types:
                export_sets = {"types":i, "model":i}
                type_list.append(export_sets)
        return type_list

        # form = GenerateAdhocFileForm(request.POST)
        # if form.is_valid():
        #     a = form.cleaned_data.get('name')
        #     a = form.cleaned_data['types']

        # portfolio_list.append(portfolios)
        # type_list.append(types)
        # date_ranges.append(date_range)

        example_path = pathlib.Path('test.json')
        example_dict = {'env': env, 'types': types}
        json_str = json.dumps(example_dict, indent=4) + '\n'
        example_path.write_text(json_str, encoding='utf-8')

    return render(request, 'toolgenerator/generate_file.html')
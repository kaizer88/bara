from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .common import *

from .forms import GenerateAdhocFileForm

import pathlib
import json

# Create your views here.

# @login_required()

import datetime
from .models import Tool

def generate_file(request, context=None):
    context = {}
    form = GenerateAdhocFileForm(request.POST or None)
    q = Tool.objects.all()
    if request.method == 'POST':
        types = request.POST.getlist('types')
        portfolios = request.POST.getlist('portfolios')
        stress_model = request.POST.get('stress_model')
        mcvar_model = request.POST.get('mcvar_model')
        headlines_model = request.POST.get('headlines_model')
        headline_assets_model = request.POST.get('headline_assets_model')
        date_range = request.POST.get('date_range')
        ex_weekends = request.POST.get('ex_weekends')
        # i = request.POST.get('ex_weekends')
        weekend_check = weekends_check(ex_weekends)
        # form.fields['namess'].choices = [(types, types)]
        # if form.is_valid():
        # if request.method == 'POST' and form.is_valid():
        portfolio_list = []
        export_sets = {}
        type_list = []
        # types = []
        date_ranges = []
        path = settings.FILE_PATH
        pathlib.Path(path, 'test.json')

        # form.cleaned_data['types']
        # env = request.POST.get('env')


        start_date = date_range[0:10]
        end_date = date_range[13:23]

        get_dates = workdays(start_date, end_date, ex_weekends)

        exportsets = get_export_set(types=types, stress_model=stress_model, mcvar_model=mcvar_model, headline_model=headlines_model,
                              headline_assets_model=headline_assets_model)




        json_data(portfolios, get_dates, weekend_check, exportsets)
        return redirect('dashboard')

    # context['form'] = form
    context['q'] = q
    context['a'] = ['am', 'w']
    # return render(request, 'dashboard/dashboard.html')
    return render(request, 'toolgenerator/generate_file.html', context)
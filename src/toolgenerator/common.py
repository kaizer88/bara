import datetime
from datetime import date
import pathlib
import json
from django.conf import settings

def get_export_set(types, stress_model=None, mcvar_model=None, headline_model=None, headline_assets_model=None):
    type_list = []

    for i in types:
        # export_sets = {}

        if i == "stress":
            export_sets = {"types": i, "model": stress_model}
            type_list.append(export_sets)

        elif i == "mcvar":
            export_sets = {"types": i, "model": mcvar_model}
            type_list.append(export_sets)

        elif i == "headlines":
            export_sets = {"types": i, "model": headline_model}
            type_list.append(export_sets)

        elif i == "headline_assets":
            export_sets = {"types": i, "model": headline_assets_model}
            type_list.append(export_sets)

    return type_list


def weekends_check(status):

    if status == "on":
        return True
    else:
        return False


def workdays(start, end, exclude_weekends):
    days = []
    excluded = (6, 7)
    new_start = datetime.datetime.strptime(start, "%m/%d/%Y")
    new_end = datetime.datetime.strptime(end, "%m/%d/%Y")
    while new_start.date() <= new_end.date():
        if exclude_weekends == "on":
            if new_start.isoweekday() not in excluded:
                a=new_start.date()

                days.append(str(new_start.date()))

            new_start += datetime.timedelta(days=1)
        else:
            if new_start.isoweekday():
                days.append(str(new_start.date()))
            new_start += datetime.timedelta(days=1)

    return days


def json_data(portfolios, get_dates, weekend_check, exportsets):
    path = settings.FILE_PATH
    example_path = pathlib.Path(path, 'test.json')
    example_dict = {'portfolios': portfolios, 'analysis-date': get_dates, 'exclude_weekends': weekend_check,
                    'exportsets': exportsets}
    json_str = json.dumps(example_dict, indent=4) + '\n'
    example_path.write_text(json_str, encoding='utf-8')



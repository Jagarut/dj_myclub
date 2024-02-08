from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

def index(request, year=date.today().year, month=date.today().month):
    # t = date.today()
    # month = date.strftime(t, "%b")
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year

    month_name = calendar.month_name[month]

    title = f"My Club Event Calendar - {month_name} {year}"
    cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h1>%s</h1><p>%s</p>"%(title,cal) )
    return render(request, 'events/calendar_base.html' ,{'title': title, 'cal':cal})
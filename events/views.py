from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def index(request, year, month):
    # t = date.today()
    # month = date.strftime(t, "%b")
    # year = t.year
    title = f"My Club Event Calendar - {month} {year}"
    return HttpResponse("<h1>%s</h1>"%title )
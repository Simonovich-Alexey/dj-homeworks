from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    try:
        with open(BUS_STATION_CSV, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            reader_list = [{"Name": i.get('LName'),
                            "Street": i.get('Street'),
                            "District": i.get('District')} for i in reader]

    except FileNotFoundError:
        raise f'Файл не найден'

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(reader_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

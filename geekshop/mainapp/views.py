import json
from math import prod
from django.http.request import HttpRequest
import imp
from django.shortcuts import render

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,

    })


def products(request):
    with open('./products.json', 'r') as file:
        products = json.load(file)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products,
        'menu_links': MENU_LINKS,

    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,

    })

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.

'''
Icons needed:
Almond
Oat
Not Milk
Milk
Espresso Machine
V60
Aeropress
Chemex
Decaf
Vegan
'''


class Index(View):
    def __init__(self):
        self.template_name = "index.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Products(View):
    def __init__(self):
        self.template_name = "products.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class About(View):
    def __init__(self):
        self.template_name = "about.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Menu(View):
    def __init__(self):
        self.template_name = "menu.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Coffee(View):
    def __init__(self):
        self.template_name = "coffee.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Regular(View):
    def __init__(self):
        self.template_name = "regular.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Order(View):
    def __init__(self):
        self.template_name = "order.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Profile(View):
    def __init__(self):
        self.template_name = "profile.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
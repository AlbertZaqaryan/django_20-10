from django.shortcuts import render
from .models import Car
from django.views.generic import ListView, DetailView


class CarListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        car = Car.objects.all()
        return render(request, self.template_name, {'car':car})


class CarDetailView(DetailView):
    template_name = 'home_detail.html'

    def get(self, request, slug):
        c = Car.objects.get(slug=slug)
        return render(request, self.template_name, {'c':c})
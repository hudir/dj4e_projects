from django.views import View
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from autos.models import Auto, Make

class AutoListView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()
        ctx = {
            'make_count': mc,
            'auto_list': al
        }

        return render(request, 'autos/auto_list.html', ctx)
    
class MakeListView(LoginRequiredMixin, View):
     def get(self, request):
        ml = Make.objects.all()
        ctx = {
            'make_list': ml
        }

        return render(request, 'autos/make_list.html', ctx)
     
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:auto_list')
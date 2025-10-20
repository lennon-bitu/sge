from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView
from inflow.forms import InflowForm
from .models import Inflow  # Assuming you have a Inflow model defined
from django.urls import reverse_lazy

class InflowListView(ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10  # Number of inflows per page

    def get_queryset(self):
        queryset = super().get_queryset()
        product_filter = self.request.GET.get('product', None)

        if product_filter:
            queryset = queryset.filter(product__title__icontains=product_filter)
        
        return queryset


class InflowCreateView(CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm  # Assuming you have a inflowForm defined
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'


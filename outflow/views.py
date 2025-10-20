from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView
from outflow.forms import OutflowForm
from .models import Outflow  # Assuming you have a Outflow model defined
from django.urls import reverse_lazy

class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10  # Number of outflows per page

    def get_queryset(self):
        queryset = super().get_queryset()
        product_filter = self.request.GET.get('product', None)

        if product_filter:
            queryset = queryset.filter(product__title__icontains=product_filter)
        
        return queryset


class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm  # Assuming you have a outflowForm defined
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'


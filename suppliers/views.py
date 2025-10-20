from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from suppliers.forms import SupplierForm
from .models import Supplier  # Assuming you have a supplier model defined
from django.urls import reverse_lazy

class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10  # Number of suppliers per page

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name', None)

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        
        return queryset.order_by('name')


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm  # Assuming you have a supplierForm defined
    success_url = reverse_lazy('supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'


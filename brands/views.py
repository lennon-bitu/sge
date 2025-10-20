from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from brands.forms import BrandForm
from .models import Brand  # Assuming you have a Brand model defined
from django.urls import reverse_lazy

class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10  # Number of brands per page

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name', None)

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        
        return queryset.order_by('name')


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm  # Assuming you have a BrandForm defined
    success_url = reverse_lazy('brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'


def brand_detail_ajax(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    data = {
        'name': brand.name,
        'description': brand.description,
    }
    return JsonResponse(data)

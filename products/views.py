from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from products.forms import ProductForm
from .models import Product  # Assuming you have a Product model defined
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Number of products per page

    def get_queryset(self):
        queryset = super().get_queryset()
        title_filter = self.request.GET.get('title', None)

        if title_filter:
            queryset = queryset.filter(title__icontains=title_filter)
        
        return queryset.order_by('title')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm  # Assuming you have a ProductForm defined
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


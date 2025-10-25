from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from products.forms import ProductForm
from .models import Product  # Assuming you have a Product model defined
from categories.models import Category  # Assuming you have a Category model defined
from brands.models import Brand  # Assuming you have a Brand model defined
from django.urls import reverse_lazy
from app.metrics import get_product_metrics

# from django.db.models import Q

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product_list.html'
#     context_object_name = 'products'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         filters = self.get_filters()
#         return self.apply_filters(queryset, filters).order_by('title')

#     def get_filters(self):
#         """Extrai e organiza os filtros da requisição GET."""
#         request = self.request.GET
#         return {
#             "title": request.get("title"),
#             "category_id": request.get("category"),
#             "brand_id": request.get("brand"),
#             "ean": request.get("ean"),
#             "serial_number": request.get("serial_number"),
#         }

#     def apply_filters(self, queryset, filters):
#         """Aplica dinamicamente os filtros válidos ao queryset."""
#         filter_map = {
#             "title": "title__icontains",
#             "category_id": "category__id",
#             "brand_id": "brand__id",
#             "ean": "ean__icontains",
#             "serial_number": "serial_number__icontains",
#         }

#         query = Q()
#         for key, value in filters.items():
#             if value:
#                 query &= Q(**{filter_map[key]: value})

#         return queryset.filter(query)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Number of products per page

    def get_queryset(self):
        queryset = super().get_queryset()
        title_filter = self.request.GET.get('title', None)
        category_filter = self.request.GET.get('category', None)
        brand_filter = self.request.GET.get('brand', None)
        ean_filter = self.request.GET.get('ean', None)
        serial_number_filter = self.request.GET.get('serial_number', None)

        if title_filter:
            queryset = queryset.filter(title__icontains=title_filter)
        
        if category_filter:
            queryset = queryset.filter(category__id=category_filter)
        
        if brand_filter:
            queryset = queryset.filter(brand__id=brand_filter)
        
        if ean_filter:
            queryset =queryset.filter(ean__icontains=ean_filter)
        
        if serial_number_filter:
            queryset =queryset.filter(serial_number__icontains=serial_number_filter)
        
        return queryset.order_by('title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics']  = get_product_metrics()
        return context


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


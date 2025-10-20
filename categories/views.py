from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from categories.forms import CategoryForm
from .models import Category  # Assuming you have a category model defined
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10  # Number of categories per page

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.GET.get('name', None)

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        
        return queryset.order_by('name')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm  # Assuming you have a categoryForm defined
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

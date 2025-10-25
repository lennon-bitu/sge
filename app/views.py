from django.shortcuts import render
from products.models import Product
from app.metrics import get_product_metrics

def home(request):
    
    product_metrics = get_product_metrics()
    context = {
        'product_metrics': product_metrics,
    }
    return render(request, 'pages/home.html', context)
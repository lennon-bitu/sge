from django.shortcuts import render
from products.models import Product

def home(request):
    products = Product.objects.all()
    product_metrics = {
        'total_products': products.count(),
        # Additional metrics can be calculated here
        'total_selling_price': sum(p.selling_price * p.quantity for p in products),
        'total_cost_price': sum(p.cost_price * p.quantity for p in products),
        'total_profit': sum((p.selling_price - p.cost_price) * p.quantity for p in products if p.cost_price is not None),
    }
    context = {
        'product_metrics': product_metrics,
    }
    return render(request, 'pages/home.html', context)
from products.models import Product
from django.utils.formats import number_format


def get_product_metrics():
    products = Product.objects.all()
    metrics = {
        #'total_products': products.count(),
        'total_products': sum(p.quantity for p in products),
        # Additional metrics can be calculated here
        'total_selling_price': number_format(sum(p.selling_price * p.quantity for p in products), decimal_pos=2, force_grouping=True),
        'total_cost_price': number_format(sum(p.cost_price * p.quantity for p in products), decimal_pos=2, force_grouping=True),
        'total_profit': number_format(sum((p.selling_price - p.cost_price) * p.quantity for p in products if p.cost_price is not None), decimal_pos=2, force_grouping=True),
    }
    print(metrics)

    return metrics
    



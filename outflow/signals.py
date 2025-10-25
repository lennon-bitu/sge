from django.db.models.signals import post_save
from django.dispatch import receiver  #fica ouvindo os eventos
from outflow.models import Outflow


#sender quem envia o evento - Outflow
#instance a instancia que foi criada ou alterada ou seja o objeto Outflow que contem os dados
#created se foi criada ou alterada - True ou False - caso seja criada é True - caso seja alterada é False
@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()



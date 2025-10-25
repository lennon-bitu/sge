from django.db.models.signals import post_save
from django.dispatch import receiver  #fica ouvindo os eventos
from inflow.models import Inflow

#sender quem envia o evento - Inflow 
#instance a instancia que foi criada ou alterada ou seja o objeto Inflow que contem os dados
#created se foi criada ou alterada - True ou False - caso seja criada é True - caso seja alterada é False
@receiver(post_save, sender=Inflow)
def update_produtct_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()
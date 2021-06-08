# from users.models import ProductCustomer
# from .models import Code
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# @receiver(post_save, sender=ProductCustomer)
# def post_save_generate_code(sender, instance, created, *args, **kwargs):
#     if created:
#         Code.objects.create(user=instance)

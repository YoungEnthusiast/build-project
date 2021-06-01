from django.contrib import admin
from .models import UserOrder, OrderItem, VisitorOrder, VisitorOrderItem, OrderStatus

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['product', 'price', 'quantity', 'get_cost']
    fields = ['product', 'price', 'quantity', 'get_cost']
    raw_id_fields = ['product']

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ['order_Id', 'user', 'email', 'payment_Mode', 'get_total_cost', 'schedule_Delivery', 'delivery_Type', 'order_Status', 'payment_Status', 'phone_Number', 'state', 'city', 'address', 'date_Ordered']
    search_fields = ['order_Id', 'user__username', 'email', 'payment_Mode', 'delivery_Type', 'date_Ordered', 'last_Modified', 'order_Status', 'payment_Status', 'phone_Number', 'state', 'city']
    list_filter = ['payment_Mode', 'delivery_Type', 'order_Status', 'payment_Status', 'state', 'city']
    list_display_links = ['order_Id', 'user']
    list_per_page = 10
    inlines = [OrderItemInline]

admin.site.register(UserOrder, UserOrderAdmin)

class VisitorOrderItemInline(admin.TabularInline):
    model = VisitorOrderItem
    readonly_fields = ['product', 'price', 'quantity', 'get_cost']
    fields = ['product', 'price', 'quantity', 'get_cost']
    raw_id_fields = ['product']

class VisitorOrderAdmin(admin.ModelAdmin):
    list_display = ['order_Id', 'first_Name', 'email', 'state', 'city', 'address', 'payment_Mode', 'schedule_Delivery', 'order_Status', 'payment_Status', 'date_Ordered']
    search_fields = ['order_Id', 'first_Name', 'email', 'state', 'city', 'address', 'payment_Mode', 'date_Ordered', 'order_Status', 'state', 'city', 'payment_Status']
    list_filter = ['state', 'city', 'payment_Mode', 'order_Status', 'payment_Status', 'state', 'city']
    list_display_links = ['order_Id', 'first_Name', 'email']
    list_per_page = 10
    inlines = [VisitorOrderItemInline]

admin.site.register(VisitorOrder, VisitorOrderAdmin)

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['order', 'order_Status', 'created', 'updated']
    search_fields = ['order__order_Id', 'order_Status', 'created', 'updated']
    list_filter = ['order_Status']
    list_display_links = ['order']
    list_per_page = 10

admin.site.register(OrderStatus, OrderStatusAdmin)

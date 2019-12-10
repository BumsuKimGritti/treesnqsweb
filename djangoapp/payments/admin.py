from django.contrib import admin

from payments.models import OrderItem, Order, Payment, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'order_created', 'ordered_date']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount']


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon, CouponAdmin)

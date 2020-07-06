from django.contrib import admin
from .models import FitnessPlan,Customer

@admin.register(FitnessPlan)
class FitnessPlanAdmin(admin.ModelAdmin):
    list_display = ('title','premium')
    list_filter  = ('title','premium')
    search_field = ('title')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','stripeid','stripe_subscription_id','cancel_at_period_end','membership')
    list_filter  = ('user','stripeid','stripe_subscription_id','cancel_at_period_end','membership')
    search_field = ('user','stripeid','stripe_subscription_id','cancel_at_period_end','membership')


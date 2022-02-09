from django.contrib import admin
from .models import Influencer, InfluencerEarning, AllInfluencerSale, InfluencerPayHistory


class InfluencerAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'instagram', 'email', 'phone', 'coupon']
	list_filter = ['first_name', 'last_name', 'instagram', 'email', 'phone', 'coupon']
	list_per_page = 50

class InfluencerEarningAdmin(admin.ModelAdmin):
	list_display = ['influencer', 'total_amount', 'commission_earned', 'commission_paid', 'commission_owned', 'pay']
	list_filter = ['influencer', 'total_amount', 'commission_earned']
	list_per_page = 50
	


# Register your models here.
admin.site.register(Influencer, InfluencerAdmin)
admin.site.register(InfluencerEarning, InfluencerEarningAdmin)
admin.site.register(AllInfluencerSale)
admin.site.register(InfluencerPayHistory)
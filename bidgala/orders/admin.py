from django.contrib import admin
from django.db import models
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.shortcuts import render
from django.conf import settings


from .models import Inquiry

# Register your models here.
class InquiryInfo(models.Model):
    class Meta:
        verbose_name_plural = 'All the Inquiries'

@staff_member_required
def inquiry_view(request):
    inquiry_obj = Inquiry.objects.filter(accepted=False).filter(product__sold=False).order_by('created_date')
    return render(request, 'custom_admin/custom_inquiry.html', {'inquiry' : inquiry_obj, 'BASE_IMG_URL':settings.BASE_AWS_IMG_URL})


class InquiryInfoAdmin(admin.ModelAdmin):
    model = Inquiry

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('custom/', inquiry_view, name=view_name),
        ]


admin.site.register(InquiryInfo, InquiryInfoAdmin)
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
import logging
import sys


from .models import Influencer, InfluencerEarning, InfluencerPayHistory


@user_passes_test(lambda u: u.is_superuser)
def pay_influencer(request):
	id = request.POST['influencer']
	obj = Influencer.objects.filter(id=id)[0]
	try:
		with transaction.atomic():
			ie_obj = InfluencerEarning.objects.filter(influencer=obj)[0]

			if ie_obj.commission_owned > 0:
				ie_obj.commission_paid = ie_obj.commission_owned + ie_obj.commission_paid

				iph_obj = InfluencerPayHistory(influencer=obj, amount=ie_obj.commission_owned)
				iph_obj.save()

				ie_obj.commission_owned = 0
				ie_obj.save()

	except Exception as e:
		logging.getLogger("error_logger").error('Error on line {}'.format(sys.exc_info()[-1].tb_lineno) + ' : ' +str(e))

	return redirect('/admin/influencer/influencerearning/')
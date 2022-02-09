from payments.models import Orders
from datetime import datetime, timedelta
from django.utils import timezone
from django_cron import CronJobBase, Schedule
from django.db import transaction
import logging

class OrderDecline(CronJobBase):
	
	RUN_AT_TIMES = ['23:40']
	# RUN_EVERY_MINS = 1
	RETRY_AFTER_FAILURE_MINS = 5
	MIN_NUM_FAILURES = 5

	schedule = Schedule(run_at_times=RUN_AT_TIMES, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
	code = 'cron.order_decline'


	def do(self):
		pass
		try:
			
			with transaction.atomic():
				current_time = datetime.now(tz=timezone.utc)
				obj_orders = Orders.objects.filter(tracking_number__in=['',None]).filter(order_date__lte = current_time-timedelta(days=7))
		
				for obj in obj_orders:
					ord_hld = obj.order_hold
					ord_hld.accepted = False
					ord_hld.declined = True
					ord_hld.declined_timestamp = datetime.now(tz=timezone.utc)
					ord_hld.save()
					product_in_hold = obj.order_hold.product
                    product_in_hold.available = True
                    product_in_hold.sold = False
                    product_in_hold.save()
				obj_orders.delete()
			
		except Exception as e:
			logging.getLogger("error_logger").error("file : order_decline.py " + str(e))

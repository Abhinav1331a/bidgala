from payments.models import Orders
from datetime import datetime, timedelta

def decline_order():
	current_time = datetime.now()
	obj_orders = Orders.objects.filter(tracking_number__in=['',None]).filter(order_date__gte = current_time-timedelta(days=7))

	for obj in obj_orders:
		ord_hld = obj.order_hold
		ord_hld.accepted = False
		ord_hld.declined = True
		ord_hld.declined_timestamp = datetime.now()
		ord_hld.save()

	obj_orders.delete()


if __name__ == "__main__":
	decline_order()
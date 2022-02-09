from django.conf import settings
import logging

import aftership

def create_aftership_tracking(tracking_number):
    try:
        aftership.api_key = settings.AFTERSHIP_API_KEY

        tracking = {'tracking_number': tracking_number}
        result = aftership.tracking.create_tracking(tracking=tracking, timeout=20)

        return result['tracking']['id']
    except Exception as e:
        logging.getLogger("error_logger").error(str(e))
        raise Exception()
import os
ALLOWED_HOSTS = ['*']
# SERVER TYPE
SERVER_TYPE_PRODUCTION = False
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '^%biln49gh5ky_okx0ijye0=ix!g2w$dhduf&xy+6@r5z%=yoj'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:8001',
}
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bidgaladb',
        'USER': 'nourabiad',
        'PASSWORD': 'nono9911',
        'HOST': 'localhost'
}
}
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# SENDGRID API
SENDGRID_API_KEY='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'
FROM_EMAIL = 'info@thebidgala.com'
# S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = 'AKIAY6HUWSOLBELUCZXX'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'thebidgaala'
AWS_S3_FILE_OVERWRITE = False
AWS_DEAFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_QUERYSTRING_AUTH = False
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# FOR MAILCHIMP
MAILCHIMP_API_KEY = '09875d1b308463ae7e976155968049b5-us17'
MAILCHIMP_DATA_CENTER = 'us17'
MAILCHIMP_EMAIL_LIST_ID = '6065e477d7'

# IMAGE URL BASE
BASE_AWS_IMG_URL = "https://thebidgaala.s3.amazonaws.com/"
# STRIPE
STRIPE_PUBLISHABLE_KEY = 'pk_test_51H3kSfHHZ5vYGxsH7BLZU7Fh7MjkJwvn5BNOua049UMWDeSj80lOCOG4yi868IEP3SI9EEjWGqUBk0LfWEPjDqCR00cnVDZBTH'
STRIPE_SECRET_KEY = 'sk_test_51H3kSfHHZ5vYGxsHZ1mr4ER4QM9l2M7H1pg6pditLEjClQnirXcrNoFuZALtQY6yVa85iaQ4743ShhVALcs2x2FM00dxtsQe1n'
STRIPE_CONNECT_CLIENT_ID = 'ca_Hd0iwfksO7ljYLBzu4BCXjENGcoOsaAM'
STRIPE_AUTH_URL = 'https://connect.stripe.com/oauth/authorize'
STRIPE_CALLBACK_URL = f'https://localhost:8001/payments/oauth/callback/'
STRIPE_TOKEN_URL = 'https://connect.stripe.com/oauth/token'

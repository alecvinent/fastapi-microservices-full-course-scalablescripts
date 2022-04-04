from decouple import config

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_PASS = config('REDIS_PASS')
REDIS_DB = config('REDIS_DB', default=0, cast=int)
REDIS_DATA_URL = "redis://@%s:%s" % (REDIS_HOST, REDIS_PORT)

# access
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]

# routes
PRODUCTS_BASE_ROUTE = '/products'

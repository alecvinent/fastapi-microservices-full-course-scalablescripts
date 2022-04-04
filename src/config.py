from decouple import config

# products
APP_PRODUCT_HOST = config('APP_PRODUCT_HOST', default='0.0.0.0')
APP_PRODUCT_PORT = config('APP_PRODUCT_PORT', default=8000, cast=int)

# inventory
APP_INVENTORY_HOST = config('APP_INVENTORY_HOST', default='0.0.0.0')
APP_INVENTORY_PORT = config('APP_INVENTORY_PORT', default=8001, cast=int)

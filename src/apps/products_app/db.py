from redis_om import get_redis_connection

from .config import REDIS_DATA_URL, REDIS_HOST, REDIS_PORT,REDIS_DB

redis_instance = get_redis_connection(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password='',
    db=REDIS_DB,
    decode_responses=True
)
# redis_instance.set("hello", "world")
print('Redis is connected', redis_instance.ping())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import product_route
from .config import PRODUCTS_BASE_ROUTE, ALLOWED_ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# routes
app.include_router(router=product_route.router, prefix=PRODUCTS_BASE_ROUTE, tags=['Products'])

# @app.on_event("startup")
# async def startup():
#     r = aioredis.from_url(REDIS_DATA_URL, encoding="utf8", decode_responses=True)
#     FastAPICache.init(RedisBackend(r), prefix="fastapi-cache")

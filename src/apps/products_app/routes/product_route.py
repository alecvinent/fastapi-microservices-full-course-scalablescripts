from fastapi import APIRouter

from ..schemas import Product
from src.core import response_format

router = APIRouter()


@router.get("/", summary='')
async def get_all():
    return response_format(data=[format(pk) for pk in Product.all_pks()])


@router.post("/", summary='')
async def create(product: Product):
    exists = Product.find(Product.name == product.name).first()
    if exists:
        return response_format(is_error=True, message='Already in')

    return response_format(data=product.save(), message='OK')


@router.get("/{pk}", summary='')
async def get_one(pk: str) -> dict:
    product = Product.get(pk=pk)
    return response_format(data=format(product.pk), message='Getting one row')


@router.delete("/{pk}", summary='')
async def delete_one(pk: str):
    return response_format(data=Product.delete(pk=pk))


def format(pk: str) -> dict:
    product = Product.get(pk=pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

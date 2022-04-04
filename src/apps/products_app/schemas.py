from redis_om import HashModel, Field

from .db import redis_instance

class HashObject(HashModel):
    @classmethod
    def get_class_key(cls):  # type: ignore
        return cls.make_key(cls._meta.primary_key_pattern.format(pk=""))


class Product(HashObject):
    name: str = Field(index=True)
    price: float
    quantity: int

    class Meta:
        database: redis_instance

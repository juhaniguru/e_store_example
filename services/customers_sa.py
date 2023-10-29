from typing import Annotated

from fastapi import Depends

from services.base import BaseService


def init_customer_service():
    return CustomersSA()


CustomerService = Annotated[BaseService, Depends(init_customer_service)]


class CustomersSA(BaseService):
    def __init__(self):
        super(CustomersSA, self).__init__()

    def get_all(self):
        return [
            {'id': 1, 'first_name': 'Asko'}
        ]

    def get_by_id(self, _id: int):
        return {'id': 1, 'first_name': 'Asko'}

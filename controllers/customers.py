from fastapi import APIRouter

from services.customers_sa import CustomerService

router = APIRouter(
    prefix='/api/v1/customers',
    tags=['customers']
)


@router.get('/')
async def get_customers(service: CustomerService):
    return service.get_all()


@router.get('/{id}')
async def get_customer(_id: int, service: CustomerService):
    return service.get_by_id(_id)

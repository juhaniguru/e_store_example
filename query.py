import typing

import strawberry
from strawberry.types import Info

from graphql_types.customer import Customer


@strawberry.type
class Query:
    @strawberry.field
    def customers(self, info: Info) -> typing.List[Customer]:
        return [Customer(id=c['id'], first_name=c['first_name']) for c in info.context['customer'].get_all()]

    @strawberry.field
    def customer(self, info: Info, _id: strawberry.ID) -> Customer:
        c = info.context['customer'].get_by_id(_id)
        return Customer(id=c['id'], first_name=c['first_name'])

import typing

import strawberry
from strawberry.types import Info

from graphql_types.customer import Customer


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_customer(self, info: Info, first_name: str, last_name: str) -> Customer:
        return info.context['customer'].add_customer(first_name, last_name)

    @strawberry.mutation
    def delete_customer(self, info: Info, _id: int) -> bool:
        return info.context['customer'].delete(_id)
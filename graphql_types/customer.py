import strawberry


@strawberry.type
class Customer:
    id: int
    first_name: str
    last_name: str

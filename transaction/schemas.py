from typing import Annotated

from typing import Optional

from pydantic import UUID4, Field

from pydantic import PositiveFloat

from contrib.schemas import BaseSchema

from contrib.schemas import OutMixin

from datetime import date

class Transaction(BaseSchema):
    name: Annotated[str, Field(description="Name of the person who carried out the transaction.", example="Victor Brito",max_length=100)]
    category: Annotated[str, Field(description="Category of the place of that transaction.", example="Restaurant", max_length=50)]
    place: Annotated[str, Field(description="Name place of this transaction.", example="Domes Burguer", max_length=100)]
    value: Annotated[PositiveFloat, Field(description="Value of this transaction.", example=96.53)]
    card: Annotated[str , Field(description="Credit card name.", example="Mastercard Willbank",max_length=50)]
    transaction_date: Annotated[date, Field(description="Transaction date.", example='2024-04-30')]
    status: Annotated[str, Field(description="Status of this transacation.", example="Open", max_length=20)]

class TransactionOut(Transaction,OutMixin):
    super


class TransactionIn(Transaction):
    super

class TransactionUpdate(BaseSchema):
    status: Annotated[Optional[str], Field(None,description="Status of this transacation.", example="Open", max_length=20)]
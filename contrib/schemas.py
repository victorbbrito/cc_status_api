from typing import Annotated

from pydantic import BaseModel

from pydantic import Field

from pydantic import UUID4

from datetime import datetime

class BaseSchema(BaseModel):

    class Config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="Identifier")]
    created_at: Annotated[datetime, Field(description="Created at date")]

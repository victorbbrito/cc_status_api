from uuid import uuid4

from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PG_UUID 

from sqlalchemy import UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),default=uuid4,nullable=False)

# id é mapeado como um UUID que é por default um uuid4, nullable = False ( n pode ser vazio)
# é o basemodel por que todos os modelos de dados do banco teram um id -> e será do tipo uuid4


from contrib.models import BaseModel

from sqlalchemy import String

from sqlalchemy import Float

from sqlalchemy import Integer

from sqlalchemy import Date

from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from datetime import date

from datetime import datetime


class TransactionModel(BaseModel):
    __tablename__ = 'transactions'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(50),nullable=True)
    place: Mapped[str] = mapped_column(String(100),nullable=False)
    value: Mapped[str] = mapped_column(Float, nullable=False)
    card: Mapped[str] = mapped_column(String(50), nullable=False)
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

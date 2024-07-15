from uuid import uuid4

from fastapi import APIRouter

from fastapi import HTTPException

from fastapi import Body

from fastapi import status

from pydantic import UUID4

from sqlalchemy.future import select

from transaction.schemas import TransactionOut

from transaction.schemas import TransactionIn

from transaction.schemas import TransactionUpdate

from transaction.models import TransactionModel

from contrib.dependencies import DatabaseDependency

from datetime import datetime

from datetime import time

from datetime import UTC

router = APIRouter()


@router.post('/',summary='Create a new transaction',status_code=status.HTTP_201_CREATED,response_model=TransactionOut)
async def post(db_session: DatabaseDependency, transaction_in: TransactionIn = Body(...)) -> TransactionOut:
    
    transaction_out = TransactionOut(id=uuid4(),created_at=datetime.now(UTC).replace(tzinfo=None),**transaction_in.model_dump())
    transaction_model = TransactionModel(**transaction_out.model_dump())
    
    db_session.add(transaction_model)
    await db_session.commit()
    
    return transaction_out


@router.get('/', summary="Browser all transactions",status_code=status.HTTP_200_OK,response_model=list[TransactionOut])
async def query(db_session:DatabaseDependency) -> TransactionOut:
    transactions: list[TransactionOut] = (await db_session.execute(select(TransactionModel))).scalars().all()
    return [TransactionOut.model_validate(transaction) for transaction in transactions]


@router.patch('/{id}',summary='Edit status of transaction',status_code=status.HTTP_200_OK,response_model=TransactionOut)
async def query(id: UUID4, db_session: DatabaseDependency, transaction_update: TransactionUpdate = Body(...)) -> TransactionOut:
    transaction: TransactionOut = (await db_session.execute(select(TransactionModel).filter_by(id=id))).scalars().first()
    
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No transaction was found with the given id: {id}')
    
    transaction_update = transaction_update.model_dump(exclude_unset=True)
    
    for key,value in transaction_update.items():
        setattr(transaction,key,value)
    
    await db_session.commit()
    
    await db_session.refresh(transaction)
    
    return transaction


@router.delete('/{id}',summary='Delete a transaction by id',status_code=status.HTTP_204_NO_CONTENT)
async def query(id: UUID4, db_session: DatabaseDependency) -> None:
    transaction: TransactionOut = (await db_session.execute(select(TransactionModel).filter_by(id=id))).scalars().first()
    
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No transaction was found with the given id: {id}')
    
    await db_session.delete(transaction)
    
    await db_session.commit()
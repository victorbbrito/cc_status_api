from fastapi import APIRouter

from transaction.controller import router as cc_router

api_router = APIRouter()
api_router.include_router(cc_router, prefix="/transaction", tags=["transaction"])

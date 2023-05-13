from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, customers, headquarters

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(customers.router, prefix='/customers', tags=['Customers'])
api_router.include_router(headquarters.router, prefix='/headquarters', tags=['Headquarters'])

from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, customers, headquarters, areas, services, treatments

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(customers.router, prefix="/customers", tags=["Customers"])
api_router.include_router(headquarters.router, prefix="/headquarters", tags=["Headquarters"])
api_router.include_router(areas.router, prefix="/areas", tags=["Areas"])
api_router.include_router(treatments.router, prefix="/treatments", tags=["Treatments"])
api_router.include_router(services.router, prefix="/services", tags=["Services"])

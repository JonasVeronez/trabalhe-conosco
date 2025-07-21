from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.dashboard import  DashboardResponse
from crud import dashboard as crud_dashboard

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model= DashboardResponse)
async def obter_dashboard(db: AsyncSession = Depends(get_db)):
    return await crud_dashboard.obter_dashboard(db)

from typing import Optional, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.teams import db_actions
from app.routes.users import get_user_id
from app.pydantic_models.teams import TeamModel, TeamModelResponse
from app.db.base import get_db


teams_router = APIRouter(prefix="/teams", tags=["Team"])


@teams_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_team(
    user_id: Annotated[str, Depends(get_user_id)],
    team_model: TeamModel,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    await db_actions.create_team(user_id=user_id, team_model=team_model, db=db)


@teams_router.get("/{team_id}/", status_code=status.HTTP_202_ACCEPTED, response_model=TeamModelResponse)
async def get_team(
    team_id: str,
    user_id: Annotated[str, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)]
):
    team = await db_actions.get_team(team_id=team_id, db=db)
    if not team_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Команда з таким ID не зареєстрована")
    return team


@teams_router.get("/", status_code=status.HTTP_202_ACCEPTED, response_model=List[TeamModelResponse])
async def get_teams(
    user_id: Annotated[str, Depends(get_user_id)],
    db: Annotated[AsyncSession, Depends(get_db)],
    private: Optional[bool] = Query(None)
):
    return await db_actions.get_teams(private=private, db=db)


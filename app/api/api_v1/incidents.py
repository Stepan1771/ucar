from typing import Annotated, List

from fastapi import APIRouter, Depends, Path
from starlette import status

from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper

from core.config import settings

from core.schemas.incident import (
    IncidentResponse,
    IncidentCreate,
    IncidentUpdateStatus,
)

from crud.incidents import crud_incidents


router = APIRouter(
    prefix=settings.api.v1.incidents,
    tags=["Incidents"],
)


@router.get(
    "/all",
    response_model=List[IncidentResponse],
    summary="Получить все инциденты",
    status_code=status.HTTP_200_OK,
)
async def get_all_incidents(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
):
    incidents = await crud_incidents.get_all(
        session=session,
    )
    return [
        IncidentResponse.model_validate(incident)
        for incident in incidents
    ]


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse,
    summary="Получить инцидент по ID",
    status_code=status.HTTP_200_OK,
)
async def get_incident_by_id(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        incident_id: int = Path(..., description="ID инцидента"),
):
    incident = await crud_incidents.get_by_id(
        session=session,
        model_id=incident_id,
    )
    return IncidentResponse.model_validate(incident)


@router.get(
    "/get-by-status/{incident_status}",
    response_model=List[IncidentResponse],
    summary="Получить инциденты по статусу",
    status_code=status.HTTP_200_OK,
)
async def get_incidents_by_status(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        incident_status: str = Path(..., description="Статус инцидента"),
):
    incidents = await crud_incidents.get_incidents_by_status(
        session=session,
        incident_status=str(incident_status),
    )
    return [
        IncidentResponse.model_validate(incident)
        for incident in incidents
    ]


@router.post(
    "/create-incident",
    response_model=IncidentResponse,
    summary="Создать инцидент",
    status_code=status.HTTP_201_CREATED,
)
async def create_incident(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        create_schema: IncidentCreate,
):
    incident = await crud_incidents.create_incident(
        session=session,
        create_schema=create_schema,
    )
    return IncidentResponse.model_validate(incident)


@router.patch(
    "/update-status",
    response_model=IncidentResponse,
    summary="Обновить статус инцидента",
    status_code=status.HTTP_200_OK,
)
async def update_incident_status(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        update_schema: IncidentUpdateStatus,
):
    incident = await crud_incidents.update_incident_status(
        session=session,
        update_schema=update_schema,
    )
    return IncidentResponse.model_validate(incident)


@router.delete(
    "/{incident_id}/delete",
    summary="Удалить инцидент по ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_incident(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        incident_id: int = Path(..., description="ID инцидента"),
):
    result = await crud_incidents.delete(
        session=session,
        model_id=incident_id,
    )
    return result
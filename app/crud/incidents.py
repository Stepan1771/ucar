from typing import Sequence

from fastapi import HTTPException
from starlette import status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Incident
from core.schemas.incident import IncidentCreate, IncidentUpdateStatus

from crud.base import BaseCRUD


class IncidentsCRUD(BaseCRUD[Incident, IncidentCreate, IncidentUpdateStatus]):

    @staticmethod
    async def get_incidents_by_status(
            session: AsyncSession,
            incident_status: str,
    ) -> Sequence[Incident]:
        try:
            stmt = await session.execute(
                select(Incident)
                .filter(Incident.status == incident_status)
                .order_by(Incident.date_time)
            )
            incidents = stmt.scalars().all()
            if not incidents:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Incidents with status '{incident_status}' not found",
                )
            return incidents

        except Exception as e:
            raise e


    async def update_incident_status(
            self,
            session: AsyncSession,
            update_schema: IncidentUpdateStatus,
    ) -> Incident:
        try:
            incident = await self.get_by_id(
                session=session,
                model_id=int(update_schema.id),
            )
            incident.status = update_schema.status
            await session.commit()
            await session.refresh(incident)
            return incident

        except Exception as e:
            raise e


    @staticmethod
    async def create_incident(
            session: AsyncSession,
            create_schema: IncidentCreate,
    ) -> Incident:
        try:
            incident = Incident(
                description=create_schema.description,
                finder=create_schema.finder,
            )
            session.add(incident)
            await session.commit()
            await session.refresh(incident)
            return incident

        except Exception as e:
            raise e


crud_incidents = IncidentsCRUD(Incident)
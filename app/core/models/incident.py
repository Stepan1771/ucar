from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, Index

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Incident(IntIdPkMixin, Base):
        __tablename__ = 'incidents'

        description: Mapped[str] = mapped_column(
                String(255),
                nullable=False,
        )
        status: Mapped[str] = mapped_column(
                String(20),
                nullable=False,
                index=True,
                default="created",
        )
        date_time: Mapped[str] = mapped_column(
                DateTime,
                nullable=False,
                index=True,
                default=datetime.now,
        )
        finder: Mapped[str] = mapped_column(
                String(50),
                nullable=False,
                index=True,
        )

        __table_args__ = (
                Index('ix_incidents_status_date_time', 'status', 'date_time'),
                Index('ix_incidents_finder_date_time', 'finder', 'date_time'),
        )
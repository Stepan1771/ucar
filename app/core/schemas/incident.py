from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class IncidentBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )


class IncidentCreate(BaseModel):
    description: str
    finder: str

    @field_validator("finder")
    def validate_finder(cls, value):
        finder = value.strip().lower()
        valid_finders = [
            "user",
            "operator",
            "monitoring",
            "partner",
        ]
        if finder not in valid_finders:
            raise ValueError("Incorrect finder")
        return finder


class IncidentUpdateStatus(IncidentBase):
    id: int
    status: str

    model_config = ConfigDict(
        from_attributes=True,
    )

    @field_validator("status")
    def validate_status(cls, value):
        status = value.strip().lower()
        valid_status = [
            "created",
            "check",
            "fix",
            "completed",
        ]
        if status not in valid_status:
            raise ValueError("Incorrect status")
        return status


class IncidentResponse(IncidentBase):
    id: int
    description: str
    status: str
    date_time: datetime
    finder: str

    model_config = ConfigDict(
        from_attributes=True,
    )







    






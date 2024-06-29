from pydantic import BaseModel, Field
from sqlalchemy import UUID


class CurrentUser(BaseModel):
    uuid: UUID = Field(..., description='The UUID of the current user')

    class Config:
        validate_assignment = True

from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base
from core.database.mixins import TimestampMixin, UserStampMixin


class Language(Base, TimestampMixin, UserStampMixin):
    __tablename__ = "languages"

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=lambda: uuid4()
    )
    code: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=True)
    native_name: Mapped[str] = mapped_column(String, nullable=True)
    flag: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self):
        return f"<Language(name='{self.name}', code='{self.code}')>"

    def __str__(self):
        return self.__repr__()

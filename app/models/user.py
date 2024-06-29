import enum
from uuid import uuid4

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base
from core.database.mixins import TimestampMixin, UserStampMixin


class UserType(enum.Enum):
    SELLER: str = "seller"
    BUYER: str = "buyer"
    OTHER: str = "other"


def rang():
    for i in range(1, 100):
        yield i


class User(Base, TimestampMixin, UserStampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, default=lambda: rang())
    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True),
                                       primary_key=True,
                                       unique=True,
                                       default=uuid4())
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    preferred_language: Mapped[UUID] = mapped_column(UUID(as_uuid=True),
                                                     ForeignKey(
                                                         "languages.uuid"),
                                                     nullable=True)

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return f"<User(uuid={self.uuid}, email={self.email})>"

    def __str__(self):
        return self.__repr__()

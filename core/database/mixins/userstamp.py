# pylint: skip-file

from sqlalchemy import String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column


class UserStampMixin:
    @declared_attr
    def created_by(cls):
        return mapped_column(
            String,
            nullable=False
        )

    @declared_attr
    def updated_by(cls):
        return mapped_column(
            String,
            nullable=False
        )

    @declared_attr
    def activated_by(cls):
        return mapped_column(
            String,
            nullable=False
        )

    @declared_attr
    def deleted_by(cls):
        return mapped_column(
            String,
            nullable=False
        )

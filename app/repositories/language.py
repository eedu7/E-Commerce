from sqlalchemy.dialects.postgresql import UUID

from app.models import Language
from core.repository import BaseRepository


class LanguageRepository(BaseRepository[Language]):
    """
    User repository provides all the database operations for the User model.
    """

    async def get_by_uuid(
        self, uuid: UUID, join_: set[str] | None = None
    ) -> Language | None:
        """
        Get language by uuid.

        :param uuid: UUID.
        :param join_: Join relations.
        :return: Language.
        """
        query = await self._query(join_)
        query = query.filter(Language.uuid == uuid)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._one_or_none(query)

    async def get_by_code(
        self, code: str, join_: set[str] | None = None
    ) -> Language | None:
        """
        Get language by code.

        :param code: code.
        :param join_: Join relations.
        :return: Language.
        """
        query = await self._query(join_)
        query = query.filter(Language.code == code)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._one_or_none(query)

    async def get_by_name(
        self, name: str, join_: set[str] | None = None
    ) -> Language | None:
        """
        Get language by name.

        :param name: name.
        :param join_: Join relations.
        :return: Language.
        """
        query = await self._query(join_)
        query = query.filter(Language.name == name)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._one_or_none(query)

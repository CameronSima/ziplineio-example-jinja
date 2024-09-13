import re
from ziplineio.service import Service
from services.sqlite import SqliteService


class MailingListService(Service):
    name = "mailing_list_service"

    def __init__(self, sqlite_service: SqliteService):
        self.sqlite_service = sqlite_service

    async def subscribe(self, email: str):
        res = await self.sqlite_service.execute(
            f"INSERT INTO mailing_list (email) VALUES ('{email}')"
        )
        return res

    async def unsubscribe(self, email: str):
        return self.sqlite_service.execute(
            f"DELETE FROM mailing_list WHERE email = '{email}'"
        )

    async def get_subscribers(self):
        return self.sqlite_service.execute("SELECT * FROM mailing_list")

import aiosqlite
from ziplineio.service import Service


# init the table
async def init_db():
    async with aiosqlite.connect("./zipline.db") as db:
        await db.execute(
            """       
        CREATE TABLE IF NOT EXISTS mailing_list ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL
        )
        """
        )
    await db.commit()


class SqliteService(Service):
    name = "sqlite_service"

    async def execute(self, query: str):
        async with aiosqlite.connect("./zipline.db") as db:
            await db.execute(query)

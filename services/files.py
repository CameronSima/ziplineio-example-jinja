import aiofiles
from ziplineio.service import Service


class FileService(Service):
    name = "file_service"

    async def open_file(self, path: str) -> str:
        async with aiofiles.open(path, mode="r") as f:
            return await f.read()

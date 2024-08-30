from ziplineio.service import Service
import markdown
from pygments.formatters.html import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension

from services.files import FileService


class MarkdownService(Service):
    name = "markdown_service"

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    async def markdown_to_html(self, file_path: str) -> dict:
        markdown_content = await self.file_service.open_file(file_path)
        pygments_css = HtmlFormatter().get_style_defs(".codehilite")
        html_content = markdown.markdown(
            markdown_content,
            extensions=[
                "fenced_code",
                CodeHiliteExtension(
                    linenums=False, noclasses=False, pygments_style="friendly"
                ),
            ],
            output_format="html5",
        )
        return html_content, pygments_css

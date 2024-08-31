from ziplineio import ZipLine
from ziplineio.html.jinja import jinja
from services.markdown import MarkdownService
from services.files import FileService


import uvicorn
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape(),
)

app = ZipLine()
app.static("./static")

app.inject([FileService, MarkdownService])


@app.get("/")
@jinja(env, "home.jinja")
def home(req):
    return {"current_route": "home"}


@app.get("/features")
@jinja(env, "features.jinja")
async def features(req, markdown_service: MarkdownService):
    html_content, pygments_css = await markdown_service.markdown_to_html("README.md")

    return {
        "current_route": "features",
        "content": html_content,
        "pygments_css": pygments_css,
    }


@app.not_found
@jinja(env, "404.jinja")
def not_found(req):
    return {"current_route": "404"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)

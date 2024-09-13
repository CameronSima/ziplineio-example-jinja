from ziplineio.router import Router
from ziplineio.request import Request
from ziplineio.validation.body import validate_body, BodyParam
from services.mailing_list import MailingListService
from services.sqlite import SqliteService

mailing_list_router = Router()

mailing_list_router.inject([SqliteService, MailingListService])


@mailing_list_router.post("/subscribe")
@validate_body(BodyParam("email", str, required=True))
async def subscribe(req: Request, mailing_list_service: MailingListService):
    try:
        email = req.body.get("email")
        await mailing_list_service.subscribe(email)
        return {"message": "Subscribed successfully"}
    except Exception as e:
        print(e)
        return {"message": str(e)}

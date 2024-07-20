from fastapi import FastAPI, Request
import logging
from fastapi.responses import JSONResponse
from https.controllers.sellers.route import router

app = FastAPI()


app.include_router(router)

# Logging setup
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# @app.exception_handler(Exception)
# async def general_exception_handler(request: Request, exc: Exception):
#     if app.debug:
#         logger.debug(exc)
#     else:
#         return
#     return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

from fastapi.requests import Request
from api_routes import api as api_routes
from view_routes import view as view_routes
from configs.env import getEnv

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles

import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ignore unexpected disk cache for html file 
@app.middleware("http")
async def ignoreCache(request: Request, call_next):
    response = await call_next(request)
    # if response.headers.get('Content-Type') and 'text/html' in response.headers['Content-Type']:
    response.headers['Cache-Control'] = 'no-cache'
    return response


#static files
app.mount("/public", StaticFiles(directory="public"))

# include controller
app.include_router(api_routes)
app.include_router(view_routes)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={
        'error': exc.detail
    }, status_code=exc.status_code)


@app.on_event("startup")
async def startup_event():
    sentry_sdk.init(
        dsn=getEnv().SENTRY_DSN,
        environment=getEnv().SENTRY_ENV,
    )
    app.add_middleware(SentryAsgiMiddleware)


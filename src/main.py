from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from uvicorn import run as run_server
from api import api_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan
)
app.include_router(api_v1)


@app.get('/')
async def redirect_from_main_to_docs():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    run_server('main:app', host='0.0.0.0', port=3000, reload=True)

"""Main module"""

import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)


def init_app():
    """Collects all routes"""

    web_app = FastAPI()
    web_app.include_router(user_router)

    return web_app


app = init_app()


@app.get("/", include_in_schema=False)
def interface():
    """Adds suffix '/docs' to create interface"""

    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)

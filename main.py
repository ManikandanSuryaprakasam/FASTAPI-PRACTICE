
"""Application entrypoint: FastAPI app configuration and router registration.

This module:
- Creates the FastAPI application instance.
- Includes routers for articles, users and blog endpoints.
- Registers a custom exception handler for StoryException to return a JSONResponse.
- Creates database tables on startup using SQLAlchemy models metadata.

Keep this file small: heavy logic belongs in router modules and service/db layers.
"""


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import blog_get, file, product
from router import blog_post
from router import user
from router import article
from auth import authentication
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app= FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)



@app.get('/hello')
def index():
    return "Hello World"

# Link the exception handler to display proper message in response .So that it will display response in swagger ui

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name},
    )

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#To view static files like images
app.mount("/files", StaticFiles(directory="files"), name="files")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
import routes as r

app = FastAPI(docs_url=config.documentation_url)
app.include_router(router=r.app, prefix="")

@app.get("/")
def root():
    return {"Hello": "World"}


origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

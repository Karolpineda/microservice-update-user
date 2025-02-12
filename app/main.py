from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware 
from app.controllers import user  
from app.database import engine
from app.models import Base
from app.docs import swagger_router  

app = FastAPI(
    title="Mi API",
    description="Documentatión of my API",
    version="1.0.0",
    docs_url=None,  
    redoc_url=None  
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(swagger_router)
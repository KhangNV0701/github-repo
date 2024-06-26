from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.core import settings
from src.router.content_router import router as content_router
from src.router.main_router import router as main_router
from src.router.recommend_router import router as recommendation_router
from src.router.related_items_router import router as related_items_router

app = FastAPI(title=settings.PROJECT_NAME)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(CorrelationIdMiddleware)

app.include_router(router=main_router)
app.include_router(router=content_router)
app.include_router(router=recommendation_router)
app.include_router(router=related_items_router)

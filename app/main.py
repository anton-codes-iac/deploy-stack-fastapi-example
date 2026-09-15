from fastapi import FastAPI
from app.core.config import settings

from app.core.database import Base, engine

# Create tables on startup. 
# Note: For production architectures, teams typically replace this with Alembic migrations.
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

@app.get("/health", tags=["Health"])
def health_check():
    """
    AWS Application Load Balancer (ALB) health check endpoint.
    Must return a 200 OK for Fargate to consider the task healthy.
    """
    return {"status": "ok", "project": settings.PROJECT_NAME}

@app.get("/", tags=["Root"])
def read_root():
    return {"message": f"Welcome to the {settings.PROJECT_NAME} API"}
from fastapi import FastAPI
from .settings.database import engine,session_manager
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from elrahapi.middleware.log_middleware import LoggerMiddleware
# from .myapp.router import app_myapp
from .settings.auth.routers import user_router
from .settings.auth.configs import authentication_router
from .settings.logger.router import app_logger
from .settings.logger.model import Log
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
# app.include_router(app_myapp)
app.include_router(authentication_router)
app.include_router(user_router)
app.include_router(app_logger)
app.add_middleware(
    LoggerMiddleware,
    session_manager=session_manager, LogModel=Log)
app.add_middleware(
    ErrorHandlingMiddleware,
        session_manager=session_manager,
        LogModel = Log
)

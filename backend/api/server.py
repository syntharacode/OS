from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import llm, train, logs, user
from backend.core.lifecycle import on_startup, on_shutdown

app = FastAPI(title="Synthara OS API")

# CORS setup (open for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lifecycle Hooks
@app.on_event("startup")
async def startup_event():
    on_startup()

@app.on_event("shutdown")
async def shutdown_event():
    on_shutdown()

# Include all routes
app.include_router(llm.router)
app.include_router(train.router)
app.include_router(logs.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Synthara OS is running."}
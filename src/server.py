from fastapi import FastAPI
from src.constants.metadata import FastAPIMetadata

# Create instance of FastAPIMetadata
app_metadata = FastAPIMetadata()

app = FastAPI(**app_metadata.__dict__)


@app.get("/", tags=["Health"])
def health():
    return {
        "message": "Let's commute!",
        "name": "Where's the Bus? (WTB) API",
        "version": "0.0.0",
    }
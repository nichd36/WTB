from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.constants.metadata import FastAPIMetadata
from src.utils.gtfs_utils import GTFSUtils

# Create instance of FastAPIMetadata
app_metadata = FastAPIMetadata()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init GTFS data
    gtfs_utils = GTFSUtils()

    yield


app = FastAPI(**app_metadata.__dict__, lifespan=lifespan)


@app.get("/", tags=["Health"])
def health():
    return {
        "message": "Let's commute!",
        "name": "Where's the Bus? (WTB) API",
        "version": "0.0.0",
    }
import io
import zipfile

from src.constants.source_url import GTFSDataURLs

import pandas as pd
import requests


class GTFSUtils:
    # GTFS files we currently care about, mapped to the database keys.
    GTFS_FILES = {
        "routes": "routes.txt",
        "stops": "stops.txt",
        "trips": "trips.txt",
    }

    def __init__(self):
        """
        Class to fetch GTFS (static) data from API endpoints and cache it.

        Builds a separate database per region, then fetches all regions.
        """
        self.endpoint_config = GTFSDataURLs.endpoint_config

        self.databases = {
            region: {key: {} for key in self.GTFS_FILES}
            for region in self.endpoint_config.keys()
        }

        self.fetch_all()

    def fetch_region_gtfs_data(self, region: str):
        """
        Fetch GTFS data for every provider in a region and cache it as DataFrames.

        Args:
            region: Region to fetch.
        
        Returns:
            dict: A dictionary of DataFrames for the region.
        """
        if region not in self.endpoint_config:
            raise ValueError(
                f"Unknown region '{region}'. Available: {list(self.endpoint_config)}"
            )

        db = self.databases[region]

        for provider in self.endpoint_config[region]:
            url = GTFSDataURLs.BASE_URL + GTFSDataURLs.GTFS_STATIC + provider
            print(f"Fetching data from {url}")

            response = requests.get(url)
            response.raise_for_status()

            self._load_zip_into_db(response.content, db)

        return db

    def _load_zip_into_db(self, content: bytes, db: dict):
        """
        Read the GTFS zip payload and parse the relevant files into the database.
        """
        with zipfile.ZipFile(io.BytesIO(content)) as archive:
            available = set(archive.namelist())

            for key, filename in self.GTFS_FILES.items():
                if filename not in available:
                    print(f"Skipping missing file: {filename}")
                    continue

                with archive.open(filename) as file:
                    df = pd.read_csv(file)

                # Concatenate across providers so multiple sources merge per region.
                if isinstance(db[key], pd.DataFrame):
                    db[key] = pd.concat([db[key], df], ignore_index=True)
                else:
                    db[key] = df

    def fetch_all(self):
        """
        Fetch GTFS data for all configured regions.

        Returns:
            dict: A dictionary of DataFrames for all regions.
        """
        for region in self.endpoint_config:
            self.fetch_region_gtfs_data(region)

        print(self.databases)

        return self.databases

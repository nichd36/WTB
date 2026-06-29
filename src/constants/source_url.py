from dataclasses import dataclass


@dataclass(frozen=True)
class GTFSDataURLs:
    BASE_URL: str = "https://api.data.gov.my"
    GTFS_STATIC: str = "/gtfs-static"
    GTFS_REALTIME: str = "/gtfs-realtime"

    endpoint_config = {
        "klang-valley": [
            "/prasarana?category=rapid-rail-kl",
            "/prasarana?category=rapid-bus-kl",
            "/prasarana?category=rapid-bus-mrtfeeder",
        ]
    }

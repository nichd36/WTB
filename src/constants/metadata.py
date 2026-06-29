from dataclasses import dataclass, field


@dataclass(frozen=True)
class FastAPIMetadata:
    title: str = "Where's the Bus? (WTB) API"
    summary: str = "Backend service for the WTB project"
    description: str = (
        "Aims to help provide bus passengers with a better commuting experience."
    )
    version: str = "0.0.0"
    contact: dict = field(
        default_factory=lambda: {
            "name": "Nicholas D",
            "url": "https://github.com/nichd36",
        }
    )

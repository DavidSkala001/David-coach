from dataclasses import dataclass
import os


@dataclass
class Config:
    athlete_id: str
    api_key: str


def load_config():

    athlete = os.getenv("INTERVALS_ATHLETE_ID", "")
    api = os.getenv("INTERVALS_API_KEY", "")

    return Config(
        athlete_id=athlete,
        api_key=api
    )

import os
from dataclasses import dataclass



@dataclass(frozen=True)
class MongoConfig:
    uri: str


def load_mongo_config() -> MongoConfig:
    uri = os.getenv("MONGODB_URI_SALES")

    if uri:
        return MongoConfig(
            uri=uri,
        )
    from dash_erp.config.vault import get_secrets
    secrets = get_secrets("develop")

    return MongoConfig(
        uri=secrets["MONGODB_URI_SALES"],
    )
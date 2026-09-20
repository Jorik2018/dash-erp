from pymongo import MongoClient
from pymongo.database import Database
from dash_erp.config.mongo import load_mongo_config

_client: MongoClient | None = None
_db: Database | None = None


def get_database() -> Database:
    global _client, _db

    if _db is not None:
        return _db

    config = load_mongo_config()

    _client = MongoClient(
        config.uri,
        serverSelectionTimeoutMS=5000,
    )

    _client.admin.command("ping")

    #_db = _client[config.database]
    _db = _client.get_default_database()

    return _db
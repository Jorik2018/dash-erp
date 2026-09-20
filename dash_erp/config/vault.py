import os
import hvac


VAULT_ADDR = os.getenv(
    "VAULT_ADDR",
    "http://127.0.0.1:8200",
)

VAULT_TOKEN = os.environ["VAULT_TOKEN"]

_client = hvac.Client(
    url=VAULT_ADDR,
    token=VAULT_TOKEN,
)

def get_secrets(path: str) -> dict[str, str]:
    response = _client.secrets.kv.v2.read_secret_version(
        mount_point="secret",
        path=path,
    )

    return response["data"]["data"]
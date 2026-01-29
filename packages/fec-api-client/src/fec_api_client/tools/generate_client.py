from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import httpx

API_SWAGGER_URL: str = "https://api.open.fec.gov/swagger/"
SPEC_PATH = "temp/fec.swagger.json"
CLIENT_PATH: str = "packages/fec-api-client/src/fec_api_client/generated"


def download_spec(url: str, spec_path: str) -> Path:
    path = Path(spec_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    r = httpx.get(url, timeout=60.0)
    r.raise_for_status()
    path.write_bytes(r.content)

    print(f"Downloaded spec → {spec_path}")

    return path


def generate_client(spec_path: str, client_path: str) -> Path:
    out_dir = Path(client_path)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "openapi-client-python",
            "--spec",
            spec_path,
            "--output",
            client_path,
            "--service-name",
            "fec_openapi",
        ],
        check=True,
    )

    print(f"Generated client → {out_dir}")

    return out_dir


def main() -> None:
    download_spec(API_SWAGGER_URL, SPEC_PATH)
    generate_client(SPEC_PATH, CLIENT_PATH)

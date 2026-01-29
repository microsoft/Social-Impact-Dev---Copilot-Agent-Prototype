from __future__ import annotations

import re
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


def fix_parameter_ordering(client_path: str) -> None:
    """Fix methods with required parameters after optional parameters."""
    apis_file = Path(client_path) / "fec_openapi" / "FecOpenapiAPIs.py"
    if not apis_file.exists():
        return

    content = apis_file.read_text()

    # Pattern to match method signatures with parameter issues
    # We need to reorder parameters so required ones come before optional ones
    def reorder_params(match):
        method_start = match.group(1)  # "def method_name(self, "
        params_str = match.group(2)  # all parameters
        return_type = match.group(3)  # " -> Type:"

        # Split parameters by comma, but be careful with nested types
        params = []
        current = ""
        depth = 0
        for char in params_str:
            if char in "([":
                depth += 1
            elif char in ")]":
                depth -= 1
            elif char == "," and depth == 0:
                params.append(current.strip())
                current = ""
                continue
            current += char
        if current.strip():
            params.append(current.strip())

        # Separate required and optional parameters
        required = []
        optional = []
        for param in params:
            if "=" in param:
                optional.append(param)
            else:
                required.append(param)

        # Reorder: required first, then optional
        reordered = required + optional
        return method_start + ", ".join(reordered) + return_type

    # Match method definitions with mixed parameter types
    pattern = r"(def \w+\(self, )(.*?)(\) -> requests\.Response:)"
    fixed_content = re.sub(pattern, reorder_params, content)

    apis_file.write_text(fixed_content)
    print(f"Fixed parameter ordering in {apis_file}")


def main() -> None:
    download_spec(API_SWAGGER_URL, SPEC_PATH)
    generate_client(SPEC_PATH, CLIENT_PATH)
    fix_parameter_ordering(CLIENT_PATH)

BASE_API_URL = "https://api.open.fec.gov"


class FecApiClient:
    def __init__(
        self,
        auth_token: str,
        base_url: str = BASE_API_URL,
    ):
        from fec_api_client.generated.fec_openapi import FecOpenapiAPIs

        self._client = FecOpenapiAPIs(base_url=base_url, auth_token=auth_token)

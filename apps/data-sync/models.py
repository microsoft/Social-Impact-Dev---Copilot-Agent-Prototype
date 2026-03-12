"""Request models for the data-sync function app."""

from dataclasses import dataclass

import azure.functions as func
from services import parse_comma_list


@dataclass
class SyncRequest:
    """Request model for the sync endpoint."""

    committee_ids: list[str] | None

    @classmethod
    def from_http_request(cls, req: func.HttpRequest) -> "SyncRequest":
        """Parse from HTTP request.

        Checks:
        1. Query parameter: ?committee_ids=C00703975,C00618371
        2. JSON body: {"committee_ids": ["C00703975"]}

        Returns None for committee_ids if not provided in request.
        """
        # Try query param
        if query_ids := req.params.get("committee_ids"):
            return cls(committee_ids=parse_comma_list(query_ids))

        # Try JSON body
        try:
            if body := req.get_json():
                if "committee_ids" in body:
                    ids = body["committee_ids"]
                    if isinstance(ids, list):
                        return cls(committee_ids=[str(i) for i in ids])
                    if isinstance(ids, str):
                        return cls(committee_ids=parse_comma_list(ids))
        except ValueError:
            pass

        return cls(committee_ids=None)

from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Candidate(BaseModel):
    """
    Strongly-typed model class for Candidate
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def active_through(self) -> int:
        """Get active_through"""
        return self._data.get("active_through")
    @active_through.setter
    def active_through(self, value: int):
        """Set active_through"""
        self._data["active_through"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def candidate_inactive(self) -> bool:
        """Get candidate_inactive"""
        return self._data.get("candidate_inactive")
    @candidate_inactive.setter
    def candidate_inactive(self, value: bool):
        """Set candidate_inactive"""
        self._data["candidate_inactive"] = value

    @property
    def candidate_status(self) -> str:
        """Get candidate_status"""
        return self._data.get("candidate_status")
    @candidate_status.setter
    def candidate_status(self, value: str):
        """Set candidate_status"""
        self._data["candidate_status"] = value

    @property
    def cycles(self) -> List[int]:
        """Get cycles"""
        return self._data.get("cycles")
    @cycles.setter
    def cycles(self, value: List[int]):
        """Set cycles"""
        self._data["cycles"] = value

    @property
    def district(self) -> str:
        """Get district"""
        return self._data.get("district")
    @district.setter
    def district(self, value: str):
        """Set district"""
        self._data["district"] = value

    @property
    def district_number(self) -> int:
        """Get district_number"""
        return self._data.get("district_number")
    @district_number.setter
    def district_number(self, value: int):
        """Set district_number"""
        self._data["district_number"] = value

    @property
    def election_districts(self) -> List[str]:
        """Get election_districts"""
        return self._data.get("election_districts")
    @election_districts.setter
    def election_districts(self, value: List[str]):
        """Set election_districts"""
        self._data["election_districts"] = value

    @property
    def election_years(self) -> List[int]:
        """Get election_years"""
        return self._data.get("election_years")
    @election_years.setter
    def election_years(self, value: List[int]):
        """Set election_years"""
        self._data["election_years"] = value

    @property
    def federal_funds_flag(self) -> bool:
        """Get federal_funds_flag"""
        return self._data.get("federal_funds_flag")
    @federal_funds_flag.setter
    def federal_funds_flag(self, value: bool):
        """Set federal_funds_flag"""
        self._data["federal_funds_flag"] = value

    @property
    def first_file_date(self) -> str:
        """Get first_file_date"""
        return self._data.get("first_file_date")
    @first_file_date.setter
    def first_file_date(self, value: str):
        """Set first_file_date"""
        self._data["first_file_date"] = value

    @property
    def has_raised_funds(self) -> bool:
        """Get has_raised_funds"""
        return self._data.get("has_raised_funds")
    @has_raised_funds.setter
    def has_raised_funds(self, value: bool):
        """Set has_raised_funds"""
        self._data["has_raised_funds"] = value

    @property
    def inactive_election_years(self) -> List[int]:
        """Get inactive_election_years"""
        return self._data.get("inactive_election_years")
    @inactive_election_years.setter
    def inactive_election_years(self, value: List[int]):
        """Set inactive_election_years"""
        self._data["inactive_election_years"] = value

    @property
    def incumbent_challenge(self) -> str:
        """Get incumbent_challenge"""
        return self._data.get("incumbent_challenge")
    @incumbent_challenge.setter
    def incumbent_challenge(self, value: str):
        """Set incumbent_challenge"""
        self._data["incumbent_challenge"] = value

    @property
    def incumbent_challenge_full(self) -> str:
        """Get incumbent_challenge_full"""
        return self._data.get("incumbent_challenge_full")
    @incumbent_challenge_full.setter
    def incumbent_challenge_full(self, value: str):
        """Set incumbent_challenge_full"""
        self._data["incumbent_challenge_full"] = value

    @property
    def last_f2_date(self) -> str:
        """Get last_f2_date"""
        return self._data.get("last_f2_date")
    @last_f2_date.setter
    def last_f2_date(self, value: str):
        """Set last_f2_date"""
        self._data["last_f2_date"] = value

    @property
    def last_file_date(self) -> str:
        """Get last_file_date"""
        return self._data.get("last_file_date")
    @last_file_date.setter
    def last_file_date(self, value: str):
        """Set last_file_date"""
        self._data["last_file_date"] = value

    @property
    def load_date(self) -> str:
        """Get load_date"""
        return self._data.get("load_date")
    @load_date.setter
    def load_date(self, value: str):
        """Set load_date"""
        self._data["load_date"] = value

    @property
    def name(self) -> str:
        """Get name"""
        return self._data.get("name")
    @name.setter
    def name(self, value: str):
        """Set name"""
        self._data["name"] = value

    @property
    def office(self) -> str:
        """Get office"""
        return self._data.get("office")
    @office.setter
    def office(self, value: str):
        """Set office"""
        self._data["office"] = value

    @property
    def office_full(self) -> str:
        """Get office_full"""
        return self._data.get("office_full")
    @office_full.setter
    def office_full(self, value: str):
        """Set office_full"""
        self._data["office_full"] = value

    @property
    def party(self) -> str:
        """Get party"""
        return self._data.get("party")
    @party.setter
    def party(self, value: str):
        """Set party"""
        self._data["party"] = value

    @property
    def party_full(self) -> str:
        """Get party_full"""
        return self._data.get("party_full")
    @party_full.setter
    def party_full(self, value: str):
        """Set party_full"""
        self._data["party_full"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

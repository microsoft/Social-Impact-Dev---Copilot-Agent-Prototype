from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CandidateHistoryTotal(BaseModel):
    """
    Strongly-typed model class for CandidateHistoryTotal
    
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
    def address_city(self) -> str:
        """Get address_city"""
        return self._data.get("address_city")
    @address_city.setter
    def address_city(self, value: str):
        """Set address_city"""
        self._data["address_city"] = value

    @property
    def address_state(self) -> str:
        """Get address_state"""
        return self._data.get("address_state")
    @address_state.setter
    def address_state(self, value: str):
        """Set address_state"""
        self._data["address_state"] = value

    @property
    def address_street_1(self) -> str:
        """Get address_street_1"""
        return self._data.get("address_street_1")
    @address_street_1.setter
    def address_street_1(self, value: str):
        """Set address_street_1"""
        self._data["address_street_1"] = value

    @property
    def address_street_2(self) -> str:
        """Get address_street_2"""
        return self._data.get("address_street_2")
    @address_street_2.setter
    def address_street_2(self, value: str):
        """Set address_street_2"""
        self._data["address_street_2"] = value

    @property
    def address_zip(self) -> str:
        """Get address_zip"""
        return self._data.get("address_zip")
    @address_zip.setter
    def address_zip(self, value: str):
        """Set address_zip"""
        self._data["address_zip"] = value

    @property
    def candidate_election_year(self) -> int:
        """Get candidate_election_year"""
        return self._data.get("candidate_election_year")
    @candidate_election_year.setter
    def candidate_election_year(self, value: int):
        """Set candidate_election_year"""
        self._data["candidate_election_year"] = value

    @property
    def candidate_first_name(self) -> str:
        """Get candidate_first_name"""
        return self._data.get("candidate_first_name")
    @candidate_first_name.setter
    def candidate_first_name(self, value: str):
        """Set candidate_first_name"""
        self._data["candidate_first_name"] = value

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
    def candidate_last_name(self) -> str:
        """Get candidate_last_name"""
        return self._data.get("candidate_last_name")
    @candidate_last_name.setter
    def candidate_last_name(self, value: str):
        """Set candidate_last_name"""
        self._data["candidate_last_name"] = value

    @property
    def candidate_middle_name(self) -> str:
        """Get candidate_middle_name"""
        return self._data.get("candidate_middle_name")
    @candidate_middle_name.setter
    def candidate_middle_name(self, value: str):
        """Set candidate_middle_name"""
        self._data["candidate_middle_name"] = value

    @property
    def candidate_prefix(self) -> str:
        """Get candidate_prefix"""
        return self._data.get("candidate_prefix")
    @candidate_prefix.setter
    def candidate_prefix(self, value: str):
        """Set candidate_prefix"""
        self._data["candidate_prefix"] = value

    @property
    def candidate_status(self) -> str:
        """Get candidate_status"""
        return self._data.get("candidate_status")
    @candidate_status.setter
    def candidate_status(self, value: str):
        """Set candidate_status"""
        self._data["candidate_status"] = value

    @property
    def candidate_suffix(self) -> str:
        """Get candidate_suffix"""
        return self._data.get("candidate_suffix")
    @candidate_suffix.setter
    def candidate_suffix(self, value: str):
        """Set candidate_suffix"""
        self._data["candidate_suffix"] = value

    @property
    def cash_on_hand_end_period(self) -> float:
        """Get cash_on_hand_end_period"""
        return self._data.get("cash_on_hand_end_period")
    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, value: float):
        """Set cash_on_hand_end_period"""
        self._data["cash_on_hand_end_period"] = value

    @property
    def coverage_end_date(self) -> str:
        """Get coverage_end_date"""
        return self._data.get("coverage_end_date")
    @coverage_end_date.setter
    def coverage_end_date(self, value: str):
        """Set coverage_end_date"""
        self._data["coverage_end_date"] = value

    @property
    def coverage_start_date(self) -> str:
        """Get coverage_start_date"""
        return self._data.get("coverage_start_date")
    @coverage_start_date.setter
    def coverage_start_date(self, value: str):
        """Set coverage_start_date"""
        self._data["coverage_start_date"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def cycles(self) -> List[int]:
        """Get cycles"""
        return self._data.get("cycles")
    @cycles.setter
    def cycles(self, value: List[int]):
        """Set cycles"""
        self._data["cycles"] = value

    @property
    def debts_owed_by_committee(self) -> float:
        """Get debts_owed_by_committee"""
        return self._data.get("debts_owed_by_committee")
    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, value: float):
        """Set debts_owed_by_committee"""
        self._data["debts_owed_by_committee"] = value

    @property
    def disbursements(self) -> float:
        """Get disbursements"""
        return self._data.get("disbursements")
    @disbursements.setter
    def disbursements(self, value: float):
        """Set disbursements"""
        self._data["disbursements"] = value

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
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def election_years(self) -> List[int]:
        """Get election_years"""
        return self._data.get("election_years")
    @election_years.setter
    def election_years(self, value: List[int]):
        """Set election_years"""
        self._data["election_years"] = value

    @property
    def fec_cycles_in_election(self) -> List[int]:
        """Get fec_cycles_in_election"""
        return self._data.get("fec_cycles_in_election")
    @fec_cycles_in_election.setter
    def fec_cycles_in_election(self, value: List[int]):
        """Set fec_cycles_in_election"""
        self._data["fec_cycles_in_election"] = value

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
    def flags(self) -> str:
        """Get flags"""
        return self._data.get("flags")
    @flags.setter
    def flags(self, value: str):
        """Set flags"""
        self._data["flags"] = value

    @property
    def has_raised_funds(self) -> bool:
        """Get has_raised_funds"""
        return self._data.get("has_raised_funds")
    @has_raised_funds.setter
    def has_raised_funds(self, value: bool):
        """Set has_raised_funds"""
        self._data["has_raised_funds"] = value

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
    def individual_itemized_contributions(self) -> float:
        """Get individual_itemized_contributions"""
        return self._data.get("individual_itemized_contributions")
    @individual_itemized_contributions.setter
    def individual_itemized_contributions(self, value: float):
        """Set individual_itemized_contributions"""
        self._data["individual_itemized_contributions"] = value

    @property
    def is_election(self) -> bool:
        """Get is_election"""
        return self._data.get("is_election")
    @is_election.setter
    def is_election(self, value: bool):
        """Set is_election"""
        self._data["is_election"] = value

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
    def other_political_committee_contributions(self) -> float:
        """Get other_political_committee_contributions"""
        return self._data.get("other_political_committee_contributions")
    @other_political_committee_contributions.setter
    def other_political_committee_contributions(self, value: float):
        """Set other_political_committee_contributions"""
        self._data["other_political_committee_contributions"] = value

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
    def receipts(self) -> float:
        """Get receipts"""
        return self._data.get("receipts")
    @receipts.setter
    def receipts(self, value: float):
        """Set receipts"""
        self._data["receipts"] = value

    @property
    def rounded_election_years(self) -> List[int]:
        """Get rounded_election_years"""
        return self._data.get("rounded_election_years")
    @rounded_election_years.setter
    def rounded_election_years(self, value: List[int]):
        """Set rounded_election_years"""
        self._data["rounded_election_years"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def state_full(self) -> str:
        """Get state_full"""
        return self._data.get("state_full")
    @state_full.setter
    def state_full(self, value: str):
        """Set state_full"""
        self._data["state_full"] = value

    @property
    def transfers_from_other_authorized_committee(self) -> float:
        """Get transfers_from_other_authorized_committee"""
        return self._data.get("transfers_from_other_authorized_committee")
    @transfers_from_other_authorized_committee.setter
    def transfers_from_other_authorized_committee(self, value: float):
        """Set transfers_from_other_authorized_committee"""
        self._data["transfers_from_other_authorized_committee"] = value

    @property
    def two_year_period(self) -> int:
        """Get two_year_period"""
        return self._data.get("two_year_period")
    @two_year_period.setter
    def two_year_period(self, value: int):
        """Set two_year_period"""
        self._data["two_year_period"] = value

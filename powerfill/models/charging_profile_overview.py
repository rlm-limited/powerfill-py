from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargingProfileOverview")


@_attrs_define
class ChargingProfileOverview:
    """
    Attributes:
        charging_profile_pk (int | Unset):
        description (str | Unset):
        profile_kind (str | Unset):
        profile_purpose (str | Unset):
        recurrency_kind (str | Unset):
        stack_level (int | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):
    """

    charging_profile_pk: int | Unset = UNSET
    description: str | Unset = UNSET
    profile_kind: str | Unset = UNSET
    profile_purpose: str | Unset = UNSET
    recurrency_kind: str | Unset = UNSET
    stack_level: int | Unset = UNSET
    valid_from: datetime.datetime | Unset = UNSET
    valid_to: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charging_profile_pk = self.charging_profile_pk

        description = self.description

        profile_kind = self.profile_kind

        profile_purpose = self.profile_purpose

        recurrency_kind = self.recurrency_kind

        stack_level = self.stack_level

        valid_from: str | Unset = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: str | Unset = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charging_profile_pk is not UNSET:
            field_dict["chargingProfilePk"] = charging_profile_pk
        if description is not UNSET:
            field_dict["description"] = description
        if profile_kind is not UNSET:
            field_dict["profileKind"] = profile_kind
        if profile_purpose is not UNSET:
            field_dict["profilePurpose"] = profile_purpose
        if recurrency_kind is not UNSET:
            field_dict["recurrencyKind"] = recurrency_kind
        if stack_level is not UNSET:
            field_dict["stackLevel"] = stack_level
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charging_profile_pk = d.pop("chargingProfilePk", UNSET)

        description = d.pop("description", UNSET)

        profile_kind = d.pop("profileKind", UNSET)

        profile_purpose = d.pop("profilePurpose", UNSET)

        recurrency_kind = d.pop("recurrencyKind", UNSET)

        stack_level = d.pop("stackLevel", UNSET)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: datetime.datetime | Unset
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _valid_to = d.pop("validTo", UNSET)
        valid_to: datetime.datetime | Unset
        if isinstance(_valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to)

        charging_profile_overview = cls(
            charging_profile_pk=charging_profile_pk,
            description=description,
            profile_kind=profile_kind,
            profile_purpose=profile_purpose,
            recurrency_kind=recurrency_kind,
            stack_level=stack_level,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        charging_profile_overview.additional_properties = d
        return charging_profile_overview

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

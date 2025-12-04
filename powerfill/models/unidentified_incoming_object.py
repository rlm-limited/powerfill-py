from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnidentifiedIncomingObject")


@_attrs_define
class UnidentifiedIncomingObject:
    """
    Attributes:
        key (str | Unset):
        last_attempt_timestamp (datetime.datetime | Unset):
        number_of_attempts (int | Unset):
    """

    key: str | Unset = UNSET
    last_attempt_timestamp: datetime.datetime | Unset = UNSET
    number_of_attempts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        last_attempt_timestamp: str | Unset = UNSET
        if not isinstance(self.last_attempt_timestamp, Unset):
            last_attempt_timestamp = self.last_attempt_timestamp.isoformat()

        number_of_attempts = self.number_of_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if last_attempt_timestamp is not UNSET:
            field_dict["lastAttemptTimestamp"] = last_attempt_timestamp
        if number_of_attempts is not UNSET:
            field_dict["numberOfAttempts"] = number_of_attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _last_attempt_timestamp = d.pop("lastAttemptTimestamp", UNSET)
        last_attempt_timestamp: datetime.datetime | Unset
        if isinstance(_last_attempt_timestamp, Unset):
            last_attempt_timestamp = UNSET
        else:
            last_attempt_timestamp = isoparse(_last_attempt_timestamp)

        number_of_attempts = d.pop("numberOfAttempts", UNSET)

        unidentified_incoming_object = cls(
            key=key,
            last_attempt_timestamp=last_attempt_timestamp,
            number_of_attempts=number_of_attempts,
        )

        unidentified_incoming_object.additional_properties = d
        return unidentified_incoming_object

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeterValues")


@_attrs_define
class MeterValues:
    """
    Attributes:
        format_ (str | Unset):
        location (str | Unset):
        measurand (str | Unset):
        phase (str | Unset):
        reading_context (str | Unset):
        unit (str | Unset):
        value (str | Unset):
        value_timestamp (datetime.datetime | Unset):
    """

    format_: str | Unset = UNSET
    location: str | Unset = UNSET
    measurand: str | Unset = UNSET
    phase: str | Unset = UNSET
    reading_context: str | Unset = UNSET
    unit: str | Unset = UNSET
    value: str | Unset = UNSET
    value_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        location = self.location

        measurand = self.measurand

        phase = self.phase

        reading_context = self.reading_context

        unit = self.unit

        value = self.value

        value_timestamp: str | Unset = UNSET
        if not isinstance(self.value_timestamp, Unset):
            value_timestamp = self.value_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if location is not UNSET:
            field_dict["location"] = location
        if measurand is not UNSET:
            field_dict["measurand"] = measurand
        if phase is not UNSET:
            field_dict["phase"] = phase
        if reading_context is not UNSET:
            field_dict["readingContext"] = reading_context
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value
        if value_timestamp is not UNSET:
            field_dict["valueTimestamp"] = value_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format", UNSET)

        location = d.pop("location", UNSET)

        measurand = d.pop("measurand", UNSET)

        phase = d.pop("phase", UNSET)

        reading_context = d.pop("readingContext", UNSET)

        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        _value_timestamp = d.pop("valueTimestamp", UNSET)
        value_timestamp: datetime.datetime | Unset
        if isinstance(_value_timestamp, Unset):
            value_timestamp = UNSET
        else:
            value_timestamp = isoparse(_value_timestamp)

        meter_values = cls(
            format_=format_,
            location=location,
            measurand=measurand,
            phase=phase,
            reading_context=reading_context,
            unit=unit,
            value=value,
            value_timestamp=value_timestamp,
        )

        meter_values.additional_properties = d
        return meter_values

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

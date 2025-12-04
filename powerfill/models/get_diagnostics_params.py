from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDiagnosticsParams")


@_attrs_define
class GetDiagnosticsParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        location (str): The URL where charge point should upload the log file Example:
            ftp://user:pass@example.com/logs/.
        retries (int | Unset): Number of times charge point should retry upload if it fails
        retry_interval (int | Unset): Interval in seconds between retry attempts
        start (datetime.datetime | Unset): Oldest timestamp to include in log file
        stop (datetime.datetime | Unset): Latest timestamp to include in log file
    """

    charge_box_id_list: list[str]
    location: str
    retries: int | Unset = UNSET
    retry_interval: int | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    stop: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        location = self.location

        retries = self.retries

        retry_interval = self.retry_interval

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        stop: str | Unset = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "location": location,
            }
        )
        if retries is not UNSET:
            field_dict["retries"] = retries
        if retry_interval is not UNSET:
            field_dict["retryInterval"] = retry_interval
        if start is not UNSET:
            field_dict["start"] = start
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        location = d.pop("location")

        retries = d.pop("retries", UNSET)

        retry_interval = d.pop("retryInterval", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _stop = d.pop("stop", UNSET)
        stop: datetime.datetime | Unset
        if isinstance(_stop, Unset):
            stop = UNSET
        else:
            stop = isoparse(_stop)

        get_diagnostics_params = cls(
            charge_box_id_list=charge_box_id_list,
            location=location,
            retries=retries,
            retry_interval=retry_interval,
            start=start,
            stop=stop,
        )

        get_diagnostics_params.additional_properties = d
        return get_diagnostics_params

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

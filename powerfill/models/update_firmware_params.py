from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFirmwareParams")


@_attrs_define
class UpdateFirmwareParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        location (str): URL where charge point can download the firmware Example: https://firmware.example.com/v2.3.bin.
        retrieve_date_time (datetime.datetime): When charge point should start downloading firmware
        retries (int | Unset): Number of download retry attempts
        retry_interval (int | Unset): Interval in seconds between retry attempts
    """

    charge_box_id_list: list[str]
    location: str
    retrieve_date_time: datetime.datetime
    retries: int | Unset = UNSET
    retry_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        location = self.location

        retrieve_date_time = self.retrieve_date_time.isoformat()

        retries = self.retries

        retry_interval = self.retry_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "location": location,
                "retrieveDateTime": retrieve_date_time,
            }
        )
        if retries is not UNSET:
            field_dict["retries"] = retries
        if retry_interval is not UNSET:
            field_dict["retryInterval"] = retry_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        location = d.pop("location")

        retrieve_date_time = isoparse(d.pop("retrieveDateTime"))

        retries = d.pop("retries", UNSET)

        retry_interval = d.pop("retryInterval", UNSET)

        update_firmware_params = cls(
            charge_box_id_list=charge_box_id_list,
            location=location,
            retrieve_date_time=retrieve_date_time,
            retries=retries,
            retry_interval=retry_interval,
        )

        update_firmware_params.additional_properties = d
        return update_firmware_params

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_composite_schedule_response_status import (
    GetCompositeScheduleResponseStatus,
    check_get_composite_schedule_response_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charging_schedule import ChargingSchedule


T = TypeVar("T", bound="GetCompositeScheduleResponse")


@_attrs_define
class GetCompositeScheduleResponse:
    """
    Attributes:
        status (GetCompositeScheduleResponseStatus):
        charging_schedule (ChargingSchedule | Unset):
        connector_id (int | Unset):
        schedule_start (datetime.datetime | Unset):
        set_charging_schedule (bool | Unset):
        set_connector_id (bool | Unset):
        set_schedule_start (bool | Unset):
        set_status (bool | Unset):
    """

    status: GetCompositeScheduleResponseStatus
    charging_schedule: ChargingSchedule | Unset = UNSET
    connector_id: int | Unset = UNSET
    schedule_start: datetime.datetime | Unset = UNSET
    set_charging_schedule: bool | Unset = UNSET
    set_connector_id: bool | Unset = UNSET
    set_schedule_start: bool | Unset = UNSET
    set_status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        charging_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.charging_schedule, Unset):
            charging_schedule = self.charging_schedule.to_dict()

        connector_id = self.connector_id

        schedule_start: str | Unset = UNSET
        if not isinstance(self.schedule_start, Unset):
            schedule_start = self.schedule_start.isoformat()

        set_charging_schedule = self.set_charging_schedule

        set_connector_id = self.set_connector_id

        set_schedule_start = self.set_schedule_start

        set_status = self.set_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if charging_schedule is not UNSET:
            field_dict["chargingSchedule"] = charging_schedule
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if schedule_start is not UNSET:
            field_dict["scheduleStart"] = schedule_start
        if set_charging_schedule is not UNSET:
            field_dict["setChargingSchedule"] = set_charging_schedule
        if set_connector_id is not UNSET:
            field_dict["setConnectorId"] = set_connector_id
        if set_schedule_start is not UNSET:
            field_dict["setScheduleStart"] = set_schedule_start
        if set_status is not UNSET:
            field_dict["setStatus"] = set_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charging_schedule import ChargingSchedule

        d = dict(src_dict)
        status = check_get_composite_schedule_response_status(d.pop("status"))

        _charging_schedule = d.pop("chargingSchedule", UNSET)
        charging_schedule: ChargingSchedule | Unset
        if isinstance(_charging_schedule, Unset):
            charging_schedule = UNSET
        else:
            charging_schedule = ChargingSchedule.from_dict(_charging_schedule)

        connector_id = d.pop("connectorId", UNSET)

        _schedule_start = d.pop("scheduleStart", UNSET)
        schedule_start: datetime.datetime | Unset
        if isinstance(_schedule_start, Unset):
            schedule_start = UNSET
        else:
            schedule_start = isoparse(_schedule_start)

        set_charging_schedule = d.pop("setChargingSchedule", UNSET)

        set_connector_id = d.pop("setConnectorId", UNSET)

        set_schedule_start = d.pop("setScheduleStart", UNSET)

        set_status = d.pop("setStatus", UNSET)

        get_composite_schedule_response = cls(
            status=status,
            charging_schedule=charging_schedule,
            connector_id=connector_id,
            schedule_start=schedule_start,
            set_charging_schedule=set_charging_schedule,
            set_connector_id=set_connector_id,
            set_schedule_start=set_schedule_start,
            set_status=set_status,
        )

        get_composite_schedule_response.additional_properties = d
        return get_composite_schedule_response

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

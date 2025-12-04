from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.charging_profile_form_charging_profile_kind import (
    ChargingProfileFormChargingProfileKind,
    check_charging_profile_form_charging_profile_kind,
)
from ..models.charging_profile_form_charging_profile_purpose import (
    ChargingProfileFormChargingProfilePurpose,
    check_charging_profile_form_charging_profile_purpose,
)
from ..models.charging_profile_form_charging_rate_unit import (
    ChargingProfileFormChargingRateUnit,
    check_charging_profile_form_charging_rate_unit,
)
from ..models.charging_profile_form_recurrency_kind import (
    ChargingProfileFormRecurrencyKind,
    check_charging_profile_form_recurrency_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_period import SchedulePeriod


T = TypeVar("T", bound="ChargingProfileForm")


@_attrs_define
class ChargingProfileForm:
    """
    Attributes:
        charging_profile_kind (ChargingProfileFormChargingProfileKind):
        charging_profile_purpose (ChargingProfileFormChargingProfilePurpose):
        charging_rate_unit (ChargingProfileFormChargingRateUnit):
        stack_level (int):
        charging_profile_pk (int | Unset):
        description (str | Unset):
        duration_in_seconds (int | Unset):
        min_charging_rate (float | Unset):
        note (str | Unset):
        recurrency_kind (ChargingProfileFormRecurrencyKind | Unset):
        schedule_periods (list[SchedulePeriod] | Unset):
        start_schedule (datetime.datetime | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):
    """

    charging_profile_kind: ChargingProfileFormChargingProfileKind
    charging_profile_purpose: ChargingProfileFormChargingProfilePurpose
    charging_rate_unit: ChargingProfileFormChargingRateUnit
    stack_level: int
    charging_profile_pk: int | Unset = UNSET
    description: str | Unset = UNSET
    duration_in_seconds: int | Unset = UNSET
    min_charging_rate: float | Unset = UNSET
    note: str | Unset = UNSET
    recurrency_kind: ChargingProfileFormRecurrencyKind | Unset = UNSET
    schedule_periods: list[SchedulePeriod] | Unset = UNSET
    start_schedule: datetime.datetime | Unset = UNSET
    valid_from: datetime.datetime | Unset = UNSET
    valid_to: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charging_profile_kind: str = self.charging_profile_kind

        charging_profile_purpose: str = self.charging_profile_purpose

        charging_rate_unit: str = self.charging_rate_unit

        stack_level = self.stack_level

        charging_profile_pk = self.charging_profile_pk

        description = self.description

        duration_in_seconds = self.duration_in_seconds

        min_charging_rate = self.min_charging_rate

        note = self.note

        recurrency_kind: str | Unset = UNSET
        if not isinstance(self.recurrency_kind, Unset):
            recurrency_kind = self.recurrency_kind

        schedule_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedule_periods, Unset):
            schedule_periods = []
            for schedule_periods_item_data in self.schedule_periods:
                schedule_periods_item = schedule_periods_item_data.to_dict()
                schedule_periods.append(schedule_periods_item)

        start_schedule: str | Unset = UNSET
        if not isinstance(self.start_schedule, Unset):
            start_schedule = self.start_schedule.isoformat()

        valid_from: str | Unset = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: str | Unset = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargingProfileKind": charging_profile_kind,
                "chargingProfilePurpose": charging_profile_purpose,
                "chargingRateUnit": charging_rate_unit,
                "stackLevel": stack_level,
            }
        )
        if charging_profile_pk is not UNSET:
            field_dict["chargingProfilePk"] = charging_profile_pk
        if description is not UNSET:
            field_dict["description"] = description
        if duration_in_seconds is not UNSET:
            field_dict["durationInSeconds"] = duration_in_seconds
        if min_charging_rate is not UNSET:
            field_dict["minChargingRate"] = min_charging_rate
        if note is not UNSET:
            field_dict["note"] = note
        if recurrency_kind is not UNSET:
            field_dict["recurrencyKind"] = recurrency_kind
        if schedule_periods is not UNSET:
            field_dict["schedulePeriods"] = schedule_periods
        if start_schedule is not UNSET:
            field_dict["startSchedule"] = start_schedule
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_period import SchedulePeriod

        d = dict(src_dict)
        charging_profile_kind = check_charging_profile_form_charging_profile_kind(d.pop("chargingProfileKind"))

        charging_profile_purpose = check_charging_profile_form_charging_profile_purpose(d.pop("chargingProfilePurpose"))

        charging_rate_unit = check_charging_profile_form_charging_rate_unit(d.pop("chargingRateUnit"))

        stack_level = d.pop("stackLevel")

        charging_profile_pk = d.pop("chargingProfilePk", UNSET)

        description = d.pop("description", UNSET)

        duration_in_seconds = d.pop("durationInSeconds", UNSET)

        min_charging_rate = d.pop("minChargingRate", UNSET)

        note = d.pop("note", UNSET)

        _recurrency_kind = d.pop("recurrencyKind", UNSET)
        recurrency_kind: ChargingProfileFormRecurrencyKind | Unset
        if isinstance(_recurrency_kind, Unset):
            recurrency_kind = UNSET
        else:
            recurrency_kind = check_charging_profile_form_recurrency_kind(_recurrency_kind)

        _schedule_periods = d.pop("schedulePeriods", UNSET)
        schedule_periods: list[SchedulePeriod] | Unset = UNSET
        if _schedule_periods is not UNSET:
            schedule_periods = []
            for schedule_periods_item_data in _schedule_periods:
                schedule_periods_item = SchedulePeriod.from_dict(schedule_periods_item_data)

                schedule_periods.append(schedule_periods_item)

        _start_schedule = d.pop("startSchedule", UNSET)
        start_schedule: datetime.datetime | Unset
        if isinstance(_start_schedule, Unset):
            start_schedule = UNSET
        else:
            start_schedule = isoparse(_start_schedule)

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

        charging_profile_form = cls(
            charging_profile_kind=charging_profile_kind,
            charging_profile_purpose=charging_profile_purpose,
            charging_rate_unit=charging_rate_unit,
            stack_level=stack_level,
            charging_profile_pk=charging_profile_pk,
            description=description,
            duration_in_seconds=duration_in_seconds,
            min_charging_rate=min_charging_rate,
            note=note,
            recurrency_kind=recurrency_kind,
            schedule_periods=schedule_periods,
            start_schedule=start_schedule,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        charging_profile_form.additional_properties = d
        return charging_profile_form

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

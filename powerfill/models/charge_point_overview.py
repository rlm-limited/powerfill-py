from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargePointOverview")


@_attrs_define
class ChargePointOverview:
    """
    Attributes:
        charge_box_id (str | Unset): The unique OCPP identifier of the Charge Point
        charge_box_pk (int | Unset): Database primary key of the Charge Point
        description (str | Unset): The description of the Charge Point
        location_latitude (float | Unset):
        location_longitude (float | Unset):
        ocpp_protocol (str | Unset): The OCPP protocol of the Charge Point
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    description: str | Unset = UNSET
    location_latitude: float | Unset = UNSET
    location_longitude: float | Unset = UNSET
    ocpp_protocol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        description = self.description

        location_latitude = self.location_latitude

        location_longitude = self.location_longitude

        ocpp_protocol = self.ocpp_protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if description is not UNSET:
            field_dict["description"] = description
        if location_latitude is not UNSET:
            field_dict["locationLatitude"] = location_latitude
        if location_longitude is not UNSET:
            field_dict["locationLongitude"] = location_longitude
        if ocpp_protocol is not UNSET:
            field_dict["ocppProtocol"] = ocpp_protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        description = d.pop("description", UNSET)

        location_latitude = d.pop("locationLatitude", UNSET)

        location_longitude = d.pop("locationLongitude", UNSET)

        ocpp_protocol = d.pop("ocppProtocol", UNSET)

        charge_point_overview = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            description=description,
            location_latitude=location_latitude,
            location_longitude=location_longitude,
            ocpp_protocol=ocpp_protocol,
        )

        charge_point_overview.additional_properties = d
        return charge_point_overview

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

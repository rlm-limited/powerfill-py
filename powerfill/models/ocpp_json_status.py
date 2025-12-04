from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ocpp_json_status_version import OcppJsonStatusVersion, check_ocpp_json_status_version
from ..types import UNSET, Unset

T = TypeVar("T", bound="OcppJsonStatus")


@_attrs_define
class OcppJsonStatus:
    """
    Attributes:
        charge_box_id (str | Unset):
        charge_box_pk (int | Unset):
        connected_since (datetime.datetime | Unset):
        version (OcppJsonStatusVersion | Unset):
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    connected_since: datetime.datetime | Unset = UNSET
    version: OcppJsonStatusVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        connected_since: str | Unset = UNSET
        if not isinstance(self.connected_since, Unset):
            connected_since = self.connected_since.isoformat()

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if connected_since is not UNSET:
            field_dict["connectedSince"] = connected_since
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        _connected_since = d.pop("connectedSince", UNSET)
        connected_since: datetime.datetime | Unset
        if isinstance(_connected_since, Unset):
            connected_since = UNSET
        else:
            connected_since = isoparse(_connected_since)

        _version = d.pop("version", UNSET)
        version: OcppJsonStatusVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = check_ocpp_json_status_version(_version)

        ocpp_json_status = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            connected_since=connected_since,
            version=version,
        )

        ocpp_json_status.additional_properties = d
        return ocpp_json_status

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

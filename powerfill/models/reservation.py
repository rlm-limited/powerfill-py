from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reservation")


@_attrs_define
class Reservation:
    """
    Attributes:
        charge_box_id (str | Unset):
        charge_box_pk (int | Unset):
        connector_id (int | Unset):
        expiry_timestamp (datetime.datetime | Unset):
        id (int | Unset):
        ocpp_id_tag (str | Unset):
        ocpp_tag_pk (int | Unset):
        start_timestamp (datetime.datetime | Unset):
        status (str | Unset):
        transaction_id (int | Unset):
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    connector_id: int | Unset = UNSET
    expiry_timestamp: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    ocpp_id_tag: str | Unset = UNSET
    ocpp_tag_pk: int | Unset = UNSET
    start_timestamp: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    transaction_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        connector_id = self.connector_id

        expiry_timestamp: str | Unset = UNSET
        if not isinstance(self.expiry_timestamp, Unset):
            expiry_timestamp = self.expiry_timestamp.isoformat()

        id = self.id

        ocpp_id_tag = self.ocpp_id_tag

        ocpp_tag_pk = self.ocpp_tag_pk

        start_timestamp: str | Unset = UNSET
        if not isinstance(self.start_timestamp, Unset):
            start_timestamp = self.start_timestamp.isoformat()

        status = self.status

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if expiry_timestamp is not UNSET:
            field_dict["expiryTimestamp"] = expiry_timestamp
        if id is not UNSET:
            field_dict["id"] = id
        if ocpp_id_tag is not UNSET:
            field_dict["ocppIdTag"] = ocpp_id_tag
        if ocpp_tag_pk is not UNSET:
            field_dict["ocppTagPk"] = ocpp_tag_pk
        if start_timestamp is not UNSET:
            field_dict["startTimestamp"] = start_timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        _expiry_timestamp = d.pop("expiryTimestamp", UNSET)
        expiry_timestamp: datetime.datetime | Unset
        if isinstance(_expiry_timestamp, Unset):
            expiry_timestamp = UNSET
        else:
            expiry_timestamp = isoparse(_expiry_timestamp)

        id = d.pop("id", UNSET)

        ocpp_id_tag = d.pop("ocppIdTag", UNSET)

        ocpp_tag_pk = d.pop("ocppTagPk", UNSET)

        _start_timestamp = d.pop("startTimestamp", UNSET)
        start_timestamp: datetime.datetime | Unset
        if isinstance(_start_timestamp, Unset):
            start_timestamp = UNSET
        else:
            start_timestamp = isoparse(_start_timestamp)

        status = d.pop("status", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        reservation = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            connector_id=connector_id,
            expiry_timestamp=expiry_timestamp,
            id=id,
            ocpp_id_tag=ocpp_id_tag,
            ocpp_tag_pk=ocpp_tag_pk,
            start_timestamp=start_timestamp,
            status=status,
            transaction_id=transaction_id,
        )

        reservation.additional_properties = d
        return reservation

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

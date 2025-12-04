from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.connector_status_ocpp_protocol import ConnectorStatusOcppProtocol, check_connector_status_ocpp_protocol
from ..models.connector_status_status import ConnectorStatusStatus, check_connector_status_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorStatus")


@_attrs_define
class ConnectorStatus:
    """
    Attributes:
        charge_box_id (str | Unset):
        charge_box_pk (int | Unset):
        connector_id (int | Unset):
        error_code (str | Unset):
        json_and_disconnected (bool | Unset): This is true, if the chargeBox this connector belongs to is a WS/JSON
            station and it is disconnected at the moment of retrieving the status.
        ocpp_protocol (ConnectorStatusOcppProtocol | Unset):
        status (ConnectorStatusStatus | Unset):
        status_timestamp (datetime.datetime | Unset):
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    connector_id: int | Unset = UNSET
    error_code: str | Unset = UNSET
    json_and_disconnected: bool | Unset = UNSET
    ocpp_protocol: ConnectorStatusOcppProtocol | Unset = UNSET
    status: ConnectorStatusStatus | Unset = UNSET
    status_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        connector_id = self.connector_id

        error_code = self.error_code

        json_and_disconnected = self.json_and_disconnected

        ocpp_protocol: str | Unset = UNSET
        if not isinstance(self.ocpp_protocol, Unset):
            ocpp_protocol = self.ocpp_protocol

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        status_timestamp: str | Unset = UNSET
        if not isinstance(self.status_timestamp, Unset):
            status_timestamp = self.status_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if json_and_disconnected is not UNSET:
            field_dict["jsonAndDisconnected"] = json_and_disconnected
        if ocpp_protocol is not UNSET:
            field_dict["ocppProtocol"] = ocpp_protocol
        if status is not UNSET:
            field_dict["status"] = status
        if status_timestamp is not UNSET:
            field_dict["statusTimestamp"] = status_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        json_and_disconnected = d.pop("jsonAndDisconnected", UNSET)

        _ocpp_protocol = d.pop("ocppProtocol", UNSET)
        ocpp_protocol: ConnectorStatusOcppProtocol | Unset
        if isinstance(_ocpp_protocol, Unset):
            ocpp_protocol = UNSET
        else:
            ocpp_protocol = check_connector_status_ocpp_protocol(_ocpp_protocol)

        _status = d.pop("status", UNSET)
        status: ConnectorStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_connector_status_status(_status)

        _status_timestamp = d.pop("statusTimestamp", UNSET)
        status_timestamp: datetime.datetime | Unset
        if isinstance(_status_timestamp, Unset):
            status_timestamp = UNSET
        else:
            status_timestamp = isoparse(_status_timestamp)

        connector_status = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            connector_id=connector_id,
            error_code=error_code,
            json_and_disconnected=json_and_disconnected,
            ocpp_protocol=ocpp_protocol,
            status=status,
            status_timestamp=status_timestamp,
        )

        connector_status.additional_properties = d
        return connector_status

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

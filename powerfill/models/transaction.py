from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_stop_event_actor import TransactionStopEventActor, check_transaction_stop_event_actor
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """For active transactions, all 'stop'-prefixed fields would be null.
    The energy consumed during the transaction can be calculated by subtracting the 'startValue' from the 'stopValue'.
    The unit of the 'startValue' and 'stopValue' is watt-hours (Wh).

        Attributes:
            charge_box_id (str | Unset): The identifier of the charge box at which the transaction took place
            charge_box_pk (int | Unset): PK of the charge box at which the transaction took place
            connector_id (int | Unset): Connector ID of the charge box at which the transaction took place
            id (int | Unset): PK of the transaction
            ocpp_id_tag (str | Unset): The Ocpp Tag used in the transaction
            ocpp_tag_pk (int | Unset): PK of the OCPP tag used in the transaction
            start_timestamp (datetime.datetime | Unset): The timestamp at which the transaction started
            start_value (str | Unset): The meter value reading at the start of the transaction
            stop_event_actor (TransactionStopEventActor | Unset): The actor who stopped the transaction
            stop_reason (str | Unset): The reason for the transaction being stopped
            stop_timestamp (datetime.datetime | Unset): The timestamp at which the transaction ended
            stop_value (str | Unset): The meter value reading at the end of the transaction
            user_id (int | Unset): The ID of the user who owns the Ocpp Tag associated with this transaction
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    connector_id: int | Unset = UNSET
    id: int | Unset = UNSET
    ocpp_id_tag: str | Unset = UNSET
    ocpp_tag_pk: int | Unset = UNSET
    start_timestamp: datetime.datetime | Unset = UNSET
    start_value: str | Unset = UNSET
    stop_event_actor: TransactionStopEventActor | Unset = UNSET
    stop_reason: str | Unset = UNSET
    stop_timestamp: datetime.datetime | Unset = UNSET
    stop_value: str | Unset = UNSET
    user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        connector_id = self.connector_id

        id = self.id

        ocpp_id_tag = self.ocpp_id_tag

        ocpp_tag_pk = self.ocpp_tag_pk

        start_timestamp: str | Unset = UNSET
        if not isinstance(self.start_timestamp, Unset):
            start_timestamp = self.start_timestamp.isoformat()

        start_value = self.start_value

        stop_event_actor: str | Unset = UNSET
        if not isinstance(self.stop_event_actor, Unset):
            stop_event_actor = self.stop_event_actor

        stop_reason = self.stop_reason

        stop_timestamp: str | Unset = UNSET
        if not isinstance(self.stop_timestamp, Unset):
            stop_timestamp = self.stop_timestamp.isoformat()

        stop_value = self.stop_value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if id is not UNSET:
            field_dict["id"] = id
        if ocpp_id_tag is not UNSET:
            field_dict["ocppIdTag"] = ocpp_id_tag
        if ocpp_tag_pk is not UNSET:
            field_dict["ocppTagPk"] = ocpp_tag_pk
        if start_timestamp is not UNSET:
            field_dict["startTimestamp"] = start_timestamp
        if start_value is not UNSET:
            field_dict["startValue"] = start_value
        if stop_event_actor is not UNSET:
            field_dict["stopEventActor"] = stop_event_actor
        if stop_reason is not UNSET:
            field_dict["stopReason"] = stop_reason
        if stop_timestamp is not UNSET:
            field_dict["stopTimestamp"] = stop_timestamp
        if stop_value is not UNSET:
            field_dict["stopValue"] = stop_value
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        id = d.pop("id", UNSET)

        ocpp_id_tag = d.pop("ocppIdTag", UNSET)

        ocpp_tag_pk = d.pop("ocppTagPk", UNSET)

        _start_timestamp = d.pop("startTimestamp", UNSET)
        start_timestamp: datetime.datetime | Unset
        if isinstance(_start_timestamp, Unset):
            start_timestamp = UNSET
        else:
            start_timestamp = isoparse(_start_timestamp)

        start_value = d.pop("startValue", UNSET)

        _stop_event_actor = d.pop("stopEventActor", UNSET)
        stop_event_actor: TransactionStopEventActor | Unset
        if isinstance(_stop_event_actor, Unset):
            stop_event_actor = UNSET
        else:
            stop_event_actor = check_transaction_stop_event_actor(_stop_event_actor)

        stop_reason = d.pop("stopReason", UNSET)

        _stop_timestamp = d.pop("stopTimestamp", UNSET)
        stop_timestamp: datetime.datetime | Unset
        if isinstance(_stop_timestamp, Unset):
            stop_timestamp = UNSET
        else:
            stop_timestamp = isoparse(_stop_timestamp)

        stop_value = d.pop("stopValue", UNSET)

        user_id = d.pop("userId", UNSET)

        transaction = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            connector_id=connector_id,
            id=id,
            ocpp_id_tag=ocpp_id_tag,
            ocpp_tag_pk=ocpp_tag_pk,
            start_timestamp=start_timestamp,
            start_value=start_value,
            stop_event_actor=stop_event_actor,
            stop_reason=stop_reason,
            stop_timestamp=stop_timestamp,
            stop_value=stop_value,
            user_id=user_id,
        )

        transaction.additional_properties = d
        return transaction

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_message_params_trigger_message import (
    TriggerMessageParamsTriggerMessage,
    check_trigger_message_params_trigger_message,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerMessageParams")


@_attrs_define
class TriggerMessageParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        trigger_message (TriggerMessageParamsTriggerMessage):
        connector_id (int | Unset):
    """

    charge_box_id_list: list[str]
    trigger_message: TriggerMessageParamsTriggerMessage
    connector_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        trigger_message: str = self.trigger_message

        connector_id = self.connector_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "triggerMessage": trigger_message,
            }
        )
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        trigger_message = check_trigger_message_params_trigger_message(d.pop("triggerMessage"))

        connector_id = d.pop("connectorId", UNSET)

        trigger_message_params = cls(
            charge_box_id_list=charge_box_id_list,
            trigger_message=trigger_message,
            connector_id=connector_id,
        )

        trigger_message_params.additional_properties = d
        return trigger_message_params

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

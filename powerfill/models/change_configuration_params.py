from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_configuration_params_key_type import (
    ChangeConfigurationParamsKeyType,
    check_change_configuration_params_key_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeConfigurationParams")


@_attrs_define
class ChangeConfigurationParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        key_type (ChangeConfigurationParamsKeyType):
        conf_key (str | Unset): Configuration Key predefined by Ocpp Example: HeartbeatInterval.
        custom_conf_key (str | Unset): Custom Configuration Key
        value (str | Unset):
    """

    charge_box_id_list: list[str]
    key_type: ChangeConfigurationParamsKeyType
    conf_key: str | Unset = UNSET
    custom_conf_key: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        key_type: str = self.key_type

        conf_key = self.conf_key

        custom_conf_key = self.custom_conf_key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "keyType": key_type,
            }
        )
        if conf_key is not UNSET:
            field_dict["confKey"] = conf_key
        if custom_conf_key is not UNSET:
            field_dict["customConfKey"] = custom_conf_key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        key_type = check_change_configuration_params_key_type(d.pop("keyType"))

        conf_key = d.pop("confKey", UNSET)

        custom_conf_key = d.pop("customConfKey", UNSET)

        value = d.pop("value", UNSET)

        change_configuration_params = cls(
            charge_box_id_list=charge_box_id_list,
            key_type=key_type,
            conf_key=conf_key,
            custom_conf_key=custom_conf_key,
            value=value,
        )

        change_configuration_params.additional_properties = d
        return change_configuration_params

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_configuration_params_conf_key_list_item import (
    GetConfigurationParamsConfKeyListItem,
    check_get_configuration_params_conf_key_list_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConfigurationParams")


@_attrs_define
class GetConfigurationParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        comma_separated_custom_conf_keys (str | Unset): Comma separated sequence of Custom Configuration Keys
        conf_key_list (list[GetConfigurationParamsConfKeyListItem] | Unset): List of Configuration Keys predefined by
            Ocpp.
            The documented keys are the superset of all keys defined in Ocpp versions 1.2, 1.5 and 1.6.
            Therefore, not all possible keys apply to all Ocpp versions.
    """

    charge_box_id_list: list[str]
    comma_separated_custom_conf_keys: str | Unset = UNSET
    conf_key_list: list[GetConfigurationParamsConfKeyListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        comma_separated_custom_conf_keys = self.comma_separated_custom_conf_keys

        conf_key_list: list[str] | Unset = UNSET
        if not isinstance(self.conf_key_list, Unset):
            conf_key_list = []
            for conf_key_list_item_data in self.conf_key_list:
                conf_key_list_item: str = conf_key_list_item_data
                conf_key_list.append(conf_key_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
            }
        )
        if comma_separated_custom_conf_keys is not UNSET:
            field_dict["commaSeparatedCustomConfKeys"] = comma_separated_custom_conf_keys
        if conf_key_list is not UNSET:
            field_dict["confKeyList"] = conf_key_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        comma_separated_custom_conf_keys = d.pop("commaSeparatedCustomConfKeys", UNSET)

        _conf_key_list = d.pop("confKeyList", UNSET)
        conf_key_list: list[GetConfigurationParamsConfKeyListItem] | Unset = UNSET
        if _conf_key_list is not UNSET:
            conf_key_list = []
            for conf_key_list_item_data in _conf_key_list:
                conf_key_list_item = check_get_configuration_params_conf_key_list_item(conf_key_list_item_data)

                conf_key_list.append(conf_key_list_item)

        get_configuration_params = cls(
            charge_box_id_list=charge_box_id_list,
            comma_separated_custom_conf_keys=comma_separated_custom_conf_keys,
            conf_key_list=conf_key_list,
        )

        get_configuration_params.additional_properties = d
        return get_configuration_params

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

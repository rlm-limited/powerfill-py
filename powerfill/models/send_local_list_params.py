from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_local_list_params_update_type import (
    SendLocalListParamsUpdateType,
    check_send_local_list_params_update_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendLocalListParams")


@_attrs_define
class SendLocalListParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        list_version (int):
        send_empty_list_when_full (bool):
        update_type (SendLocalListParamsUpdateType):
        add_update_list (list[str] | Unset):
        delete_list (list[str] | Unset):
    """

    charge_box_id_list: list[str]
    list_version: int
    send_empty_list_when_full: bool
    update_type: SendLocalListParamsUpdateType
    add_update_list: list[str] | Unset = UNSET
    delete_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        list_version = self.list_version

        send_empty_list_when_full = self.send_empty_list_when_full

        update_type: str = self.update_type

        add_update_list: list[str] | Unset = UNSET
        if not isinstance(self.add_update_list, Unset):
            add_update_list = self.add_update_list

        delete_list: list[str] | Unset = UNSET
        if not isinstance(self.delete_list, Unset):
            delete_list = self.delete_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "listVersion": list_version,
                "sendEmptyListWhenFull": send_empty_list_when_full,
                "updateType": update_type,
            }
        )
        if add_update_list is not UNSET:
            field_dict["addUpdateList"] = add_update_list
        if delete_list is not UNSET:
            field_dict["deleteList"] = delete_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        list_version = d.pop("listVersion")

        send_empty_list_when_full = d.pop("sendEmptyListWhenFull")

        update_type = check_send_local_list_params_update_type(d.pop("updateType"))

        add_update_list = cast(list[str], d.pop("addUpdateList", UNSET))

        delete_list = cast(list[str], d.pop("deleteList", UNSET))

        send_local_list_params = cls(
            charge_box_id_list=charge_box_id_list,
            list_version=list_version,
            send_empty_list_when_full=send_empty_list_when_full,
            update_type=update_type,
            add_update_list=add_update_list,
            delete_list=delete_list,
        )

        send_local_list_params.additional_properties = d
        return send_local_list_params

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

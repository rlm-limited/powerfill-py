from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reset_params_reset_type import ResetParamsResetType, check_reset_params_reset_type

T = TypeVar("T", bound="ResetParams")


@_attrs_define
class ResetParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        reset_type (ResetParamsResetType):
    """

    charge_box_id_list: list[str]
    reset_type: ResetParamsResetType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        reset_type: str = self.reset_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "resetType": reset_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        reset_type = check_reset_params_reset_type(d.pop("resetType"))

        reset_params = cls(
            charge_box_id_list=charge_box_id_list,
            reset_type=reset_type,
        )

        reset_params.additional_properties = d
        return reset_params

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

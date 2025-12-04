from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_composite_schedule_response import GetCompositeScheduleResponse


T = TypeVar("T", bound="SuccessResponseGetCompositeScheduleResponse")


@_attrs_define
class SuccessResponseGetCompositeScheduleResponse:
    """
    Attributes:
        charge_box_id (str | Unset):
        response (GetCompositeScheduleResponse | Unset):
    """

    charge_box_id: str | Unset = UNSET
    response: GetCompositeScheduleResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_composite_schedule_response import GetCompositeScheduleResponse

        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        _response = d.pop("response", UNSET)
        response: GetCompositeScheduleResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = GetCompositeScheduleResponse.from_dict(_response)

        success_response_get_composite_schedule_response = cls(
            charge_box_id=charge_box_id,
            response=response,
        )

        success_response_get_composite_schedule_response.additional_properties = d
        return success_response_get_composite_schedule_response

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

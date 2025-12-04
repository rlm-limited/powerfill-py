from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_response_error_code import ErrorResponseErrorCode, check_error_response_error_code
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        charge_box_id (str | Unset):
        error_code (ErrorResponseErrorCode | Unset):
        error_description (str | Unset):
        error_details (str | Unset):
    """

    charge_box_id: str | Unset = UNSET
    error_code: ErrorResponseErrorCode | Unset = UNSET
    error_description: str | Unset = UNSET
    error_details: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code

        error_description = self.error_description

        error_details = self.error_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: ErrorResponseErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_error_response_error_code(_error_code)

        error_description = d.pop("errorDescription", UNSET)

        error_details = d.pop("errorDetails", UNSET)

        error_response = cls(
            charge_box_id=charge_box_id,
            error_code=error_code,
            error_description=error_description,
            error_details=error_details,
        )

        error_response.additional_properties = d
        return error_response

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

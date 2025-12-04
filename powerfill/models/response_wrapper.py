from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="ResponseWrapper")


@_attrs_define
class ResponseWrapper:
    """
    Attributes:
        configuration_keys (list[KeyValue] | Unset):
        unknown_keys (str | Unset):
    """

    configuration_keys: list[KeyValue] | Unset = UNSET
    unknown_keys: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_keys, Unset):
            configuration_keys = []
            for configuration_keys_item_data in self.configuration_keys:
                configuration_keys_item = configuration_keys_item_data.to_dict()
                configuration_keys.append(configuration_keys_item)

        unknown_keys = self.unknown_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_keys is not UNSET:
            field_dict["configurationKeys"] = configuration_keys
        if unknown_keys is not UNSET:
            field_dict["unknownKeys"] = unknown_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_value import KeyValue

        d = dict(src_dict)
        _configuration_keys = d.pop("configurationKeys", UNSET)
        configuration_keys: list[KeyValue] | Unset = UNSET
        if _configuration_keys is not UNSET:
            configuration_keys = []
            for configuration_keys_item_data in _configuration_keys:
                configuration_keys_item = KeyValue.from_dict(configuration_keys_item_data)

                configuration_keys.append(configuration_keys_item)

        unknown_keys = d.pop("unknownKeys", UNSET)

        response_wrapper = cls(
            configuration_keys=configuration_keys,
            unknown_keys=unknown_keys,
        )

        response_wrapper.additional_properties = d
        return response_wrapper

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

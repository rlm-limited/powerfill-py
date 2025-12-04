from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_user_dto import WebUserDto


T = TypeVar("T", bound="WebUserDtoList")


@_attrs_define
class WebUserDtoList:
    """
    Attributes:
        web_user_dto_list (list[WebUserDto] | Unset):
    """

    web_user_dto_list: list[WebUserDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_user_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.web_user_dto_list, Unset):
            web_user_dto_list = []
            for web_user_dto_list_item_data in self.web_user_dto_list:
                web_user_dto_list_item = web_user_dto_list_item_data.to_dict()
                web_user_dto_list.append(web_user_dto_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web_user_dto_list is not UNSET:
            field_dict["webUserDtoList"] = web_user_dto_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_user_dto import WebUserDto

        d = dict(src_dict)
        _web_user_dto_list = d.pop("webUserDtoList", UNSET)
        web_user_dto_list: list[WebUserDto] | Unset = UNSET
        if _web_user_dto_list is not UNSET:
            web_user_dto_list = []
            for web_user_dto_list_item_data in _web_user_dto_list:
                web_user_dto_list_item = WebUserDto.from_dict(web_user_dto_list_item_data)

                web_user_dto_list.append(web_user_dto_list_item)

        web_user_dto_list = cls(
            web_user_dto_list=web_user_dto_list,
        )

        web_user_dto_list.additional_properties = d
        return web_user_dto_list

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

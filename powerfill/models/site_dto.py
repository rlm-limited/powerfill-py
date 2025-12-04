from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.node import Node


T = TypeVar("T", bound="SiteDto")


@_attrs_define
class SiteDto:
    """
    Attributes:
        internal_name (str): The internal name of the site
        name (str): The name of the site
        address (Address | Unset):
        site_id (int | Unset): The unique identifier of the site
        structure (Node | Unset):
    """

    internal_name: str
    name: str
    address: Address | Unset = UNSET
    site_id: int | Unset = UNSET
    structure: Node | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_name = self.internal_name

        name = self.name

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        site_id = self.site_id

        structure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structure, Unset):
            structure = self.structure.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalName": internal_name,
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if structure is not UNSET:
            field_dict["structure"] = structure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.node import Node

        d = dict(src_dict)
        internal_name = d.pop("internalName")

        name = d.pop("name")

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        site_id = d.pop("siteId", UNSET)

        _structure = d.pop("structure", UNSET)
        structure: Node | Unset
        if isinstance(_structure, Unset):
            structure = UNSET
        else:
            structure = Node.from_dict(_structure)

        site_dto = cls(
            internal_name=internal_name,
            name=name,
            address=address,
            site_id=site_id,
            structure=structure,
        )

        site_dto.additional_properties = d
        return site_dto

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

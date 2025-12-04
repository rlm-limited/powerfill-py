from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_country import AddressCountry, check_address_country
from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        address_pk (int | Unset):
        city (str | Unset):
        country (AddressCountry | Unset):
        house_number (str | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        street (str | Unset):
        zip_code (str | Unset):
    """

    address_pk: int | Unset = UNSET
    city: str | Unset = UNSET
    country: AddressCountry | Unset = UNSET
    house_number: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    street: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_pk = self.address_pk

        city = self.city

        country: str | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country

        house_number = self.house_number

        latitude = self.latitude

        longitude = self.longitude

        street = self.street

        zip_code = self.zip_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_pk is not UNSET:
            field_dict["addressPk"] = address_pk
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if street is not UNSET:
            field_dict["street"] = street
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_pk = d.pop("addressPk", UNSET)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: AddressCountry | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = check_address_country(_country)

        house_number = d.pop("houseNumber", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        street = d.pop("street", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        address = cls(
            address_pk=address_pk,
            city=city,
            country=country,
            house_number=house_number,
            latitude=latitude,
            longitude=longitude,
            street=street,
            zip_code=zip_code,
        )

        address.additional_properties = d
        return address

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

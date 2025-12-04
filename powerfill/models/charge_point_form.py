from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.charge_point_form_security_profile import (
    ChargePointFormSecurityProfile,
    check_charge_point_form_security_profile,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="ChargePointForm")


@_attrs_define
class ChargePointForm:
    """
    Attributes:
        charge_box_id (str): This field is set when adding a charge point, and cannot be changed later.
        insert_connector_status_after_transaction_msg (bool): After a transaction start/stop message, a charging station
            might send a connector status notification, but it is not required.
            If this is enabled, SteVe will update the connector status no matter what.
        registration_status (str):
        security_profile (ChargePointFormSecurityProfile):
        address (Address | Unset):
        admin_address (str | Unset):
        auth_password (str | Unset):
        charge_box_pk (int | Unset):
        description (str | Unset):
        has_auth_password (bool | Unset):
        location_latitude (float | Unset): Deprecated because <code>address.latitude</code> replaces this field!
        location_longitude (float | Unset): Deprecated because <code>address.longitude</code> replaces this field!
        note (str | Unset):
    """

    charge_box_id: str
    insert_connector_status_after_transaction_msg: bool
    registration_status: str
    security_profile: ChargePointFormSecurityProfile
    address: Address | Unset = UNSET
    admin_address: str | Unset = UNSET
    auth_password: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    description: str | Unset = UNSET
    has_auth_password: bool | Unset = UNSET
    location_latitude: float | Unset = UNSET
    location_longitude: float | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        insert_connector_status_after_transaction_msg = self.insert_connector_status_after_transaction_msg

        registration_status = self.registration_status

        security_profile: str = self.security_profile

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        admin_address = self.admin_address

        auth_password = self.auth_password

        charge_box_pk = self.charge_box_pk

        description = self.description

        has_auth_password = self.has_auth_password

        location_latitude = self.location_latitude

        location_longitude = self.location_longitude

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxId": charge_box_id,
                "insertConnectorStatusAfterTransactionMsg": insert_connector_status_after_transaction_msg,
                "registrationStatus": registration_status,
                "securityProfile": security_profile,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if admin_address is not UNSET:
            field_dict["adminAddress"] = admin_address
        if auth_password is not UNSET:
            field_dict["authPassword"] = auth_password
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if description is not UNSET:
            field_dict["description"] = description
        if has_auth_password is not UNSET:
            field_dict["hasAuthPassword"] = has_auth_password
        if location_latitude is not UNSET:
            field_dict["locationLatitude"] = location_latitude
        if location_longitude is not UNSET:
            field_dict["locationLongitude"] = location_longitude
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address

        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId")

        insert_connector_status_after_transaction_msg = d.pop("insertConnectorStatusAfterTransactionMsg")

        registration_status = d.pop("registrationStatus")

        security_profile = check_charge_point_form_security_profile(d.pop("securityProfile"))

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        admin_address = d.pop("adminAddress", UNSET)

        auth_password = d.pop("authPassword", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        description = d.pop("description", UNSET)

        has_auth_password = d.pop("hasAuthPassword", UNSET)

        location_latitude = d.pop("locationLatitude", UNSET)

        location_longitude = d.pop("locationLongitude", UNSET)

        note = d.pop("note", UNSET)

        charge_point_form = cls(
            charge_box_id=charge_box_id,
            insert_connector_status_after_transaction_msg=insert_connector_status_after_transaction_msg,
            registration_status=registration_status,
            security_profile=security_profile,
            address=address,
            admin_address=admin_address,
            auth_password=auth_password,
            charge_box_pk=charge_box_pk,
            description=description,
            has_auth_password=has_auth_password,
            location_latitude=location_latitude,
            location_longitude=location_longitude,
            note=note,
        )

        charge_point_form.additional_properties = d
        return charge_point_form

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

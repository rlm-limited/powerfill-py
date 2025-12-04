from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.charge_point_details_security_profile import (
    ChargePointDetailsSecurityProfile,
    check_charge_point_details_security_profile,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.site_and_node_info import SiteAndNodeInfo


T = TypeVar("T", bound="ChargePointDetails")


@_attrs_define
class ChargePointDetails:
    """
    Attributes:
        charge_box_id (str): This field is set when adding a charge point, and cannot be changed later.
        insert_connector_status_after_transaction_msg (bool): After a transaction start/stop message, a charging station
            might send a connector status notification, but it is not required.
            If this is enabled, SteVe will update the connector status no matter what.
        registration_status (str):
        security_profile (ChargePointDetailsSecurityProfile):
        address (Address | Unset):
        admin_address (str | Unset):
        auth_password (str | Unset):
        charge_box_pk (int | Unset):
        charge_box_serial_number (str | Unset):
        charge_point_model (str | Unset):
        charge_point_serial_number (str | Unset):
        charge_point_vendor (str | Unset):
        description (str | Unset):
        diagnostics_status (str | Unset):
        diagnostics_status_timestamp (datetime.datetime | Unset):
        endpoint_address (str | Unset): The endpoint at which the Charge Point is reachable. Only relevant/set for
            Charge Points using SOAP
        firmware_update_timestamp (datetime.datetime | Unset):
        firmware_version (str | Unset):
        has_auth_password (bool | Unset):
        iccid (str | Unset):
        imsi (str | Unset):
        last_heartbeat_timestamp (datetime.datetime | Unset): When did last heartbeat from the Charge Point arrive?
        location_latitude (float | Unset): Deprecated because <code>address.latitude</code> replaces this field!
        location_longitude (float | Unset): Deprecated because <code>address.longitude</code> replaces this field!
        meter_serial_number (str | Unset):
        meter_type (str | Unset):
        note (str | Unset):
        ocpp_protocol (str | Unset): The OCPP protocol of the Charge Point
        site_and_node_info (SiteAndNodeInfo | Unset):
    """

    charge_box_id: str
    insert_connector_status_after_transaction_msg: bool
    registration_status: str
    security_profile: ChargePointDetailsSecurityProfile
    address: Address | Unset = UNSET
    admin_address: str | Unset = UNSET
    auth_password: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    charge_box_serial_number: str | Unset = UNSET
    charge_point_model: str | Unset = UNSET
    charge_point_serial_number: str | Unset = UNSET
    charge_point_vendor: str | Unset = UNSET
    description: str | Unset = UNSET
    diagnostics_status: str | Unset = UNSET
    diagnostics_status_timestamp: datetime.datetime | Unset = UNSET
    endpoint_address: str | Unset = UNSET
    firmware_update_timestamp: datetime.datetime | Unset = UNSET
    firmware_version: str | Unset = UNSET
    has_auth_password: bool | Unset = UNSET
    iccid: str | Unset = UNSET
    imsi: str | Unset = UNSET
    last_heartbeat_timestamp: datetime.datetime | Unset = UNSET
    location_latitude: float | Unset = UNSET
    location_longitude: float | Unset = UNSET
    meter_serial_number: str | Unset = UNSET
    meter_type: str | Unset = UNSET
    note: str | Unset = UNSET
    ocpp_protocol: str | Unset = UNSET
    site_and_node_info: SiteAndNodeInfo | Unset = UNSET
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

        charge_box_serial_number = self.charge_box_serial_number

        charge_point_model = self.charge_point_model

        charge_point_serial_number = self.charge_point_serial_number

        charge_point_vendor = self.charge_point_vendor

        description = self.description

        diagnostics_status = self.diagnostics_status

        diagnostics_status_timestamp: str | Unset = UNSET
        if not isinstance(self.diagnostics_status_timestamp, Unset):
            diagnostics_status_timestamp = self.diagnostics_status_timestamp.isoformat()

        endpoint_address = self.endpoint_address

        firmware_update_timestamp: str | Unset = UNSET
        if not isinstance(self.firmware_update_timestamp, Unset):
            firmware_update_timestamp = self.firmware_update_timestamp.isoformat()

        firmware_version = self.firmware_version

        has_auth_password = self.has_auth_password

        iccid = self.iccid

        imsi = self.imsi

        last_heartbeat_timestamp: str | Unset = UNSET
        if not isinstance(self.last_heartbeat_timestamp, Unset):
            last_heartbeat_timestamp = self.last_heartbeat_timestamp.isoformat()

        location_latitude = self.location_latitude

        location_longitude = self.location_longitude

        meter_serial_number = self.meter_serial_number

        meter_type = self.meter_type

        note = self.note

        ocpp_protocol = self.ocpp_protocol

        site_and_node_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site_and_node_info, Unset):
            site_and_node_info = self.site_and_node_info.to_dict()

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
        if charge_box_serial_number is not UNSET:
            field_dict["chargeBoxSerialNumber"] = charge_box_serial_number
        if charge_point_model is not UNSET:
            field_dict["chargePointModel"] = charge_point_model
        if charge_point_serial_number is not UNSET:
            field_dict["chargePointSerialNumber"] = charge_point_serial_number
        if charge_point_vendor is not UNSET:
            field_dict["chargePointVendor"] = charge_point_vendor
        if description is not UNSET:
            field_dict["description"] = description
        if diagnostics_status is not UNSET:
            field_dict["diagnosticsStatus"] = diagnostics_status
        if diagnostics_status_timestamp is not UNSET:
            field_dict["diagnosticsStatusTimestamp"] = diagnostics_status_timestamp
        if endpoint_address is not UNSET:
            field_dict["endpointAddress"] = endpoint_address
        if firmware_update_timestamp is not UNSET:
            field_dict["firmwareUpdateTimestamp"] = firmware_update_timestamp
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if has_auth_password is not UNSET:
            field_dict["hasAuthPassword"] = has_auth_password
        if iccid is not UNSET:
            field_dict["iccid"] = iccid
        if imsi is not UNSET:
            field_dict["imsi"] = imsi
        if last_heartbeat_timestamp is not UNSET:
            field_dict["lastHeartbeatTimestamp"] = last_heartbeat_timestamp
        if location_latitude is not UNSET:
            field_dict["locationLatitude"] = location_latitude
        if location_longitude is not UNSET:
            field_dict["locationLongitude"] = location_longitude
        if meter_serial_number is not UNSET:
            field_dict["meterSerialNumber"] = meter_serial_number
        if meter_type is not UNSET:
            field_dict["meterType"] = meter_type
        if note is not UNSET:
            field_dict["note"] = note
        if ocpp_protocol is not UNSET:
            field_dict["ocppProtocol"] = ocpp_protocol
        if site_and_node_info is not UNSET:
            field_dict["siteAndNodeInfo"] = site_and_node_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.site_and_node_info import SiteAndNodeInfo

        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId")

        insert_connector_status_after_transaction_msg = d.pop("insertConnectorStatusAfterTransactionMsg")

        registration_status = d.pop("registrationStatus")

        security_profile = check_charge_point_details_security_profile(d.pop("securityProfile"))

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        admin_address = d.pop("adminAddress", UNSET)

        auth_password = d.pop("authPassword", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        charge_box_serial_number = d.pop("chargeBoxSerialNumber", UNSET)

        charge_point_model = d.pop("chargePointModel", UNSET)

        charge_point_serial_number = d.pop("chargePointSerialNumber", UNSET)

        charge_point_vendor = d.pop("chargePointVendor", UNSET)

        description = d.pop("description", UNSET)

        diagnostics_status = d.pop("diagnosticsStatus", UNSET)

        _diagnostics_status_timestamp = d.pop("diagnosticsStatusTimestamp", UNSET)
        diagnostics_status_timestamp: datetime.datetime | Unset
        if isinstance(_diagnostics_status_timestamp, Unset):
            diagnostics_status_timestamp = UNSET
        else:
            diagnostics_status_timestamp = isoparse(_diagnostics_status_timestamp)

        endpoint_address = d.pop("endpointAddress", UNSET)

        _firmware_update_timestamp = d.pop("firmwareUpdateTimestamp", UNSET)
        firmware_update_timestamp: datetime.datetime | Unset
        if isinstance(_firmware_update_timestamp, Unset):
            firmware_update_timestamp = UNSET
        else:
            firmware_update_timestamp = isoparse(_firmware_update_timestamp)

        firmware_version = d.pop("firmwareVersion", UNSET)

        has_auth_password = d.pop("hasAuthPassword", UNSET)

        iccid = d.pop("iccid", UNSET)

        imsi = d.pop("imsi", UNSET)

        _last_heartbeat_timestamp = d.pop("lastHeartbeatTimestamp", UNSET)
        last_heartbeat_timestamp: datetime.datetime | Unset
        if isinstance(_last_heartbeat_timestamp, Unset):
            last_heartbeat_timestamp = UNSET
        else:
            last_heartbeat_timestamp = isoparse(_last_heartbeat_timestamp)

        location_latitude = d.pop("locationLatitude", UNSET)

        location_longitude = d.pop("locationLongitude", UNSET)

        meter_serial_number = d.pop("meterSerialNumber", UNSET)

        meter_type = d.pop("meterType", UNSET)

        note = d.pop("note", UNSET)

        ocpp_protocol = d.pop("ocppProtocol", UNSET)

        _site_and_node_info = d.pop("siteAndNodeInfo", UNSET)
        site_and_node_info: SiteAndNodeInfo | Unset
        if isinstance(_site_and_node_info, Unset):
            site_and_node_info = UNSET
        else:
            site_and_node_info = SiteAndNodeInfo.from_dict(_site_and_node_info)

        charge_point_details = cls(
            charge_box_id=charge_box_id,
            insert_connector_status_after_transaction_msg=insert_connector_status_after_transaction_msg,
            registration_status=registration_status,
            security_profile=security_profile,
            address=address,
            admin_address=admin_address,
            auth_password=auth_password,
            charge_box_pk=charge_box_pk,
            charge_box_serial_number=charge_box_serial_number,
            charge_point_model=charge_point_model,
            charge_point_serial_number=charge_point_serial_number,
            charge_point_vendor=charge_point_vendor,
            description=description,
            diagnostics_status=diagnostics_status,
            diagnostics_status_timestamp=diagnostics_status_timestamp,
            endpoint_address=endpoint_address,
            firmware_update_timestamp=firmware_update_timestamp,
            firmware_version=firmware_version,
            has_auth_password=has_auth_password,
            iccid=iccid,
            imsi=imsi,
            last_heartbeat_timestamp=last_heartbeat_timestamp,
            location_latitude=location_latitude,
            location_longitude=location_longitude,
            meter_serial_number=meter_serial_number,
            meter_type=meter_type,
            note=note,
            ocpp_protocol=ocpp_protocol,
            site_and_node_info=site_and_node_info,
        )

        charge_point_details.additional_properties = d
        return charge_point_details

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OcppSettings")


@_attrs_define
class OcppSettings:
    """
    Attributes:
        expiration (int): The amount of time in hours for how long a charge point should cache the authorization info of
            an idTag in its local white list, if an expiry date is not explicitly set.
            The value 0 disables this functionality (i.e. no expiry date will be set).
        heartbeat (int): The time interval in minutes for how often a charge point should request the current time from
            backend.
            The value 0 requests clients to use reasonable default values.
    """

    expiration: int
    heartbeat: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiration = self.expiration

        heartbeat = self.heartbeat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiration": expiration,
                "heartbeat": heartbeat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiration = d.pop("expiration")

        heartbeat = d.pop("heartbeat")

        ocpp_settings = cls(
            expiration=expiration,
            heartbeat=heartbeat,
        )

        ocpp_settings.additional_properties = d
        return ocpp_settings

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

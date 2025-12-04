from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.statistics_status_count_map import StatisticsStatusCountMap


T = TypeVar("T", bound="Statistics")


@_attrs_define
class Statistics:
    """
    Attributes:
        heartbeat_earlier (int | Unset):
        heartbeat_today (int | Unset):
        heartbeat_yesterday (int | Unset):
        num_charge_boxes (int | Unset):
        num_ocpp_12j_charge_boxes (int | Unset):
        num_ocpp_15j_charge_boxes (int | Unset):
        num_ocpp_16j_charge_boxes (int | Unset):
        num_ocpp_tags (int | Unset):
        num_reservations (int | Unset):
        num_sites (int | Unset):
        num_transactions (int | Unset):
        num_users (int | Unset):
        status_count_map (StatisticsStatusCountMap | Unset):
    """

    heartbeat_earlier: int | Unset = UNSET
    heartbeat_today: int | Unset = UNSET
    heartbeat_yesterday: int | Unset = UNSET
    num_charge_boxes: int | Unset = UNSET
    num_ocpp_12j_charge_boxes: int | Unset = UNSET
    num_ocpp_15j_charge_boxes: int | Unset = UNSET
    num_ocpp_16j_charge_boxes: int | Unset = UNSET
    num_ocpp_tags: int | Unset = UNSET
    num_reservations: int | Unset = UNSET
    num_sites: int | Unset = UNSET
    num_transactions: int | Unset = UNSET
    num_users: int | Unset = UNSET
    status_count_map: StatisticsStatusCountMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        heartbeat_earlier = self.heartbeat_earlier

        heartbeat_today = self.heartbeat_today

        heartbeat_yesterday = self.heartbeat_yesterday

        num_charge_boxes = self.num_charge_boxes

        num_ocpp_12j_charge_boxes = self.num_ocpp_12j_charge_boxes

        num_ocpp_15j_charge_boxes = self.num_ocpp_15j_charge_boxes

        num_ocpp_16j_charge_boxes = self.num_ocpp_16j_charge_boxes

        num_ocpp_tags = self.num_ocpp_tags

        num_reservations = self.num_reservations

        num_sites = self.num_sites

        num_transactions = self.num_transactions

        num_users = self.num_users

        status_count_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_count_map, Unset):
            status_count_map = self.status_count_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heartbeat_earlier is not UNSET:
            field_dict["heartbeatEarlier"] = heartbeat_earlier
        if heartbeat_today is not UNSET:
            field_dict["heartbeatToday"] = heartbeat_today
        if heartbeat_yesterday is not UNSET:
            field_dict["heartbeatYesterday"] = heartbeat_yesterday
        if num_charge_boxes is not UNSET:
            field_dict["numChargeBoxes"] = num_charge_boxes
        if num_ocpp_12j_charge_boxes is not UNSET:
            field_dict["numOcpp12JChargeBoxes"] = num_ocpp_12j_charge_boxes
        if num_ocpp_15j_charge_boxes is not UNSET:
            field_dict["numOcpp15JChargeBoxes"] = num_ocpp_15j_charge_boxes
        if num_ocpp_16j_charge_boxes is not UNSET:
            field_dict["numOcpp16JChargeBoxes"] = num_ocpp_16j_charge_boxes
        if num_ocpp_tags is not UNSET:
            field_dict["numOcppTags"] = num_ocpp_tags
        if num_reservations is not UNSET:
            field_dict["numReservations"] = num_reservations
        if num_sites is not UNSET:
            field_dict["numSites"] = num_sites
        if num_transactions is not UNSET:
            field_dict["numTransactions"] = num_transactions
        if num_users is not UNSET:
            field_dict["numUsers"] = num_users
        if status_count_map is not UNSET:
            field_dict["statusCountMap"] = status_count_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.statistics_status_count_map import StatisticsStatusCountMap

        d = dict(src_dict)
        heartbeat_earlier = d.pop("heartbeatEarlier", UNSET)

        heartbeat_today = d.pop("heartbeatToday", UNSET)

        heartbeat_yesterday = d.pop("heartbeatYesterday", UNSET)

        num_charge_boxes = d.pop("numChargeBoxes", UNSET)

        num_ocpp_12j_charge_boxes = d.pop("numOcpp12JChargeBoxes", UNSET)

        num_ocpp_15j_charge_boxes = d.pop("numOcpp15JChargeBoxes", UNSET)

        num_ocpp_16j_charge_boxes = d.pop("numOcpp16JChargeBoxes", UNSET)

        num_ocpp_tags = d.pop("numOcppTags", UNSET)

        num_reservations = d.pop("numReservations", UNSET)

        num_sites = d.pop("numSites", UNSET)

        num_transactions = d.pop("numTransactions", UNSET)

        num_users = d.pop("numUsers", UNSET)

        _status_count_map = d.pop("statusCountMap", UNSET)
        status_count_map: StatisticsStatusCountMap | Unset
        if isinstance(_status_count_map, Unset):
            status_count_map = UNSET
        else:
            status_count_map = StatisticsStatusCountMap.from_dict(_status_count_map)

        statistics = cls(
            heartbeat_earlier=heartbeat_earlier,
            heartbeat_today=heartbeat_today,
            heartbeat_yesterday=heartbeat_yesterday,
            num_charge_boxes=num_charge_boxes,
            num_ocpp_12j_charge_boxes=num_ocpp_12j_charge_boxes,
            num_ocpp_15j_charge_boxes=num_ocpp_15j_charge_boxes,
            num_ocpp_16j_charge_boxes=num_ocpp_16j_charge_boxes,
            num_ocpp_tags=num_ocpp_tags,
            num_reservations=num_reservations,
            num_sites=num_sites,
            num_transactions=num_transactions,
            num_users=num_users,
            status_count_map=status_count_map,
        )

        statistics.additional_properties = d
        return statistics

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

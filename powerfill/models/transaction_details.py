from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meter_values import MeterValues
    from ..models.transaction import Transaction


T = TypeVar("T", bound="TransactionDetails")


@_attrs_define
class TransactionDetails:
    """
    Attributes:
        transaction (Transaction | Unset): For active transactions, all 'stop'-prefixed fields would be null.
            The energy consumed during the transaction can be calculated by subtracting the 'startValue' from the
            'stopValue'.
            The unit of the 'startValue' and 'stopValue' is watt-hours (Wh).
        values (list[MeterValues] | Unset):
    """

    transaction: Transaction | Unset = UNSET
    values: list[MeterValues] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transaction, Unset):
            transaction = self.transaction.to_dict()

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meter_values import MeterValues
        from ..models.transaction import Transaction

        d = dict(src_dict)
        _transaction = d.pop("transaction", UNSET)
        transaction: Transaction | Unset
        if isinstance(_transaction, Unset):
            transaction = UNSET
        else:
            transaction = Transaction.from_dict(_transaction)

        _values = d.pop("values", UNSET)
        values: list[MeterValues] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = MeterValues.from_dict(values_item_data)

                values.append(values_item)

        transaction_details = cls(
            transaction=transaction,
            values=values,
        )

        transaction_details.additional_properties = d
        return transaction_details

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

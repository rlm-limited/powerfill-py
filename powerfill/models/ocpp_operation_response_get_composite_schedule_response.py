from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_exception import CallException
    from ..models.error_response import ErrorResponse
    from ..models.success_response_get_composite_schedule_response import SuccessResponseGetCompositeScheduleResponse


T = TypeVar("T", bound="OcppOperationResponseGetCompositeScheduleResponse")


@_attrs_define
class OcppOperationResponseGetCompositeScheduleResponse:
    """
    Attributes:
        error_responses (list[ErrorResponse] | Unset):
        exceptions (list[CallException] | Unset):
        success_responses (list[SuccessResponseGetCompositeScheduleResponse] | Unset):
        task_finished (bool | Unset):
        task_id (int | Unset):
    """

    error_responses: list[ErrorResponse] | Unset = UNSET
    exceptions: list[CallException] | Unset = UNSET
    success_responses: list[SuccessResponseGetCompositeScheduleResponse] | Unset = UNSET
    task_finished: bool | Unset = UNSET
    task_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.error_responses, Unset):
            error_responses = []
            for error_responses_item_data in self.error_responses:
                error_responses_item = error_responses_item_data.to_dict()
                error_responses.append(error_responses_item)

        exceptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exceptions, Unset):
            exceptions = []
            for exceptions_item_data in self.exceptions:
                exceptions_item = exceptions_item_data.to_dict()
                exceptions.append(exceptions_item)

        success_responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.success_responses, Unset):
            success_responses = []
            for success_responses_item_data in self.success_responses:
                success_responses_item = success_responses_item_data.to_dict()
                success_responses.append(success_responses_item)

        task_finished = self.task_finished

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_responses is not UNSET:
            field_dict["errorResponses"] = error_responses
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if success_responses is not UNSET:
            field_dict["successResponses"] = success_responses
        if task_finished is not UNSET:
            field_dict["taskFinished"] = task_finished
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.call_exception import CallException
        from ..models.error_response import ErrorResponse
        from ..models.success_response_get_composite_schedule_response import (
            SuccessResponseGetCompositeScheduleResponse,
        )

        d = dict(src_dict)
        _error_responses = d.pop("errorResponses", UNSET)
        error_responses: list[ErrorResponse] | Unset = UNSET
        if _error_responses is not UNSET:
            error_responses = []
            for error_responses_item_data in _error_responses:
                error_responses_item = ErrorResponse.from_dict(error_responses_item_data)

                error_responses.append(error_responses_item)

        _exceptions = d.pop("exceptions", UNSET)
        exceptions: list[CallException] | Unset = UNSET
        if _exceptions is not UNSET:
            exceptions = []
            for exceptions_item_data in _exceptions:
                exceptions_item = CallException.from_dict(exceptions_item_data)

                exceptions.append(exceptions_item)

        _success_responses = d.pop("successResponses", UNSET)
        success_responses: list[SuccessResponseGetCompositeScheduleResponse] | Unset = UNSET
        if _success_responses is not UNSET:
            success_responses = []
            for success_responses_item_data in _success_responses:
                success_responses_item = SuccessResponseGetCompositeScheduleResponse.from_dict(
                    success_responses_item_data
                )

                success_responses.append(success_responses_item)

        task_finished = d.pop("taskFinished", UNSET)

        task_id = d.pop("taskId", UNSET)

        ocpp_operation_response_get_composite_schedule_response = cls(
            error_responses=error_responses,
            exceptions=exceptions,
            success_responses=success_responses,
            task_finished=task_finished,
            task_id=task_id,
        )

        ocpp_operation_response_get_composite_schedule_response.additional_properties = d
        return ocpp_operation_response_get_composite_schedule_response

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

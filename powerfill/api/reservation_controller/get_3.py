import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_3_period_type import Get3PeriodType
from ...models.get_3_status import Get3Status
from ...models.reservation import Reservation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Get3Status | Unset = UNSET,
    period_type: Get3PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_period_type: str | Unset = UNSET
    if not isinstance(period_type, Unset):
        json_period_type = period_type

    params["periodType"] = json_period_type

    params["chargeBoxId"] = charge_box_id

    params["ocppIdTag"] = ocpp_id_tag

    params["userId"] = user_id

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/reservations",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Reservation] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Reservation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Reservation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: Get3Status | Unset = UNSET,
    period_type: Get3PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[list[Reservation]]:
    """Returns a list of reservations based on the query parameters.
    The query parameters can be used to filter the reservations.

    Args:
        status (Get3Status | Unset):
        period_type (Get3PeriodType | Unset): If 'ACTIVE' is selected, all reservations that have
            not expired yet are returned.
            In this case, the 'from' and 'to' fields will be ignored.
            If 'FROM_TO' is selected, the 'from' and 'to' fields are required.
            In this case, all reservations that have started after 'from' and did not expire before
            'to' are returned.
        charge_box_id (str | Unset): The identifier of the chargebox (i.e. charging station)
        ocpp_id_tag (str | Unset): The OCPP tag
        user_id (int | Unset): The User ID
        from_ (datetime.datetime | Unset): Show results that happened after this date/time.
            Format: ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`
        to (datetime.datetime | Unset): Show results that happened before this date/time. Format:
            ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Reservation]]
    """

    kwargs = _get_kwargs(
        status=status,
        period_type=period_type,
        charge_box_id=charge_box_id,
        ocpp_id_tag=ocpp_id_tag,
        user_id=user_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: Get3Status | Unset = UNSET,
    period_type: Get3PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> list[Reservation] | None:
    """Returns a list of reservations based on the query parameters.
    The query parameters can be used to filter the reservations.

    Args:
        status (Get3Status | Unset):
        period_type (Get3PeriodType | Unset): If 'ACTIVE' is selected, all reservations that have
            not expired yet are returned.
            In this case, the 'from' and 'to' fields will be ignored.
            If 'FROM_TO' is selected, the 'from' and 'to' fields are required.
            In this case, all reservations that have started after 'from' and did not expire before
            'to' are returned.
        charge_box_id (str | Unset): The identifier of the chargebox (i.e. charging station)
        ocpp_id_tag (str | Unset): The OCPP tag
        user_id (int | Unset): The User ID
        from_ (datetime.datetime | Unset): Show results that happened after this date/time.
            Format: ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`
        to (datetime.datetime | Unset): Show results that happened before this date/time. Format:
            ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Reservation]
    """

    return sync_detailed(
        client=client,
        status=status,
        period_type=period_type,
        charge_box_id=charge_box_id,
        ocpp_id_tag=ocpp_id_tag,
        user_id=user_id,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: Get3Status | Unset = UNSET,
    period_type: Get3PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[list[Reservation]]:
    """Returns a list of reservations based on the query parameters.
    The query parameters can be used to filter the reservations.

    Args:
        status (Get3Status | Unset):
        period_type (Get3PeriodType | Unset): If 'ACTIVE' is selected, all reservations that have
            not expired yet are returned.
            In this case, the 'from' and 'to' fields will be ignored.
            If 'FROM_TO' is selected, the 'from' and 'to' fields are required.
            In this case, all reservations that have started after 'from' and did not expire before
            'to' are returned.
        charge_box_id (str | Unset): The identifier of the chargebox (i.e. charging station)
        ocpp_id_tag (str | Unset): The OCPP tag
        user_id (int | Unset): The User ID
        from_ (datetime.datetime | Unset): Show results that happened after this date/time.
            Format: ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`
        to (datetime.datetime | Unset): Show results that happened before this date/time. Format:
            ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Reservation]]
    """

    kwargs = _get_kwargs(
        status=status,
        period_type=period_type,
        charge_box_id=charge_box_id,
        ocpp_id_tag=ocpp_id_tag,
        user_id=user_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: Get3Status | Unset = UNSET,
    period_type: Get3PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> list[Reservation] | None:
    """Returns a list of reservations based on the query parameters.
    The query parameters can be used to filter the reservations.

    Args:
        status (Get3Status | Unset):
        period_type (Get3PeriodType | Unset): If 'ACTIVE' is selected, all reservations that have
            not expired yet are returned.
            In this case, the 'from' and 'to' fields will be ignored.
            If 'FROM_TO' is selected, the 'from' and 'to' fields are required.
            In this case, all reservations that have started after 'from' and did not expire before
            'to' are returned.
        charge_box_id (str | Unset): The identifier of the chargebox (i.e. charging station)
        ocpp_id_tag (str | Unset): The OCPP tag
        user_id (int | Unset): The User ID
        from_ (datetime.datetime | Unset): Show results that happened after this date/time.
            Format: ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`
        to (datetime.datetime | Unset): Show results that happened before this date/time. Format:
            ISO 8601 with timezone. Example: `2024-08-25T14:30:00.000Z`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Reservation]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            period_type=period_type,
            charge_box_id=charge_box_id,
            ocpp_id_tag=ocpp_id_tag,
            user_id=user_id,
            from_=from_,
            to=to,
        )
    ).parsed

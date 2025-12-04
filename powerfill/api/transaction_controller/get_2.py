import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.get_2_period_type import Get2PeriodType
from ...models.get_2_type import Get2Type
from ...models.transaction import Transaction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    transaction_pk: int | Unset = UNSET,
    connector_id: int | Unset = UNSET,
    type_: Get2Type | Unset = UNSET,
    period_type: Get2PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionPk"] = transaction_pk

    params["connectorId"] = connector_id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

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
        "url": "/api/v1/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiErrorResponse | list[Transaction] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Transaction.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiErrorResponse | list[Transaction]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    transaction_pk: int | Unset = UNSET,
    connector_id: int | Unset = UNSET,
    type_: Get2Type | Unset = UNSET,
    period_type: Get2PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ApiErrorResponse | list[Transaction]]:
    """Returns a list of transactions based on the query parameters.
    The query parameters can be used to filter the transactions.

    Args:
        transaction_pk (int | Unset): Database primary key of the transaction
        connector_id (int | Unset): ID of the connector
        type_ (Get2Type | Unset): Return active or all transactions? Defaults to ALL
        period_type (Get2PeriodType | Unset): Return the time period of the transactions. If
            FROM_TO, 'from' and 'to' must be set. Additionally, 'to' must be after 'from'. Defaults to
            ALL
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
        Response[ApiErrorResponse | list[Transaction]]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
        connector_id=connector_id,
        type_=type_,
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
    transaction_pk: int | Unset = UNSET,
    connector_id: int | Unset = UNSET,
    type_: Get2Type | Unset = UNSET,
    period_type: Get2PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ApiErrorResponse | list[Transaction] | None:
    """Returns a list of transactions based on the query parameters.
    The query parameters can be used to filter the transactions.

    Args:
        transaction_pk (int | Unset): Database primary key of the transaction
        connector_id (int | Unset): ID of the connector
        type_ (Get2Type | Unset): Return active or all transactions? Defaults to ALL
        period_type (Get2PeriodType | Unset): Return the time period of the transactions. If
            FROM_TO, 'from' and 'to' must be set. Additionally, 'to' must be after 'from'. Defaults to
            ALL
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
        ApiErrorResponse | list[Transaction]
    """

    return sync_detailed(
        client=client,
        transaction_pk=transaction_pk,
        connector_id=connector_id,
        type_=type_,
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
    transaction_pk: int | Unset = UNSET,
    connector_id: int | Unset = UNSET,
    type_: Get2Type | Unset = UNSET,
    period_type: Get2PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[ApiErrorResponse | list[Transaction]]:
    """Returns a list of transactions based on the query parameters.
    The query parameters can be used to filter the transactions.

    Args:
        transaction_pk (int | Unset): Database primary key of the transaction
        connector_id (int | Unset): ID of the connector
        type_ (Get2Type | Unset): Return active or all transactions? Defaults to ALL
        period_type (Get2PeriodType | Unset): Return the time period of the transactions. If
            FROM_TO, 'from' and 'to' must be set. Additionally, 'to' must be after 'from'. Defaults to
            ALL
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
        Response[ApiErrorResponse | list[Transaction]]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
        connector_id=connector_id,
        type_=type_,
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
    transaction_pk: int | Unset = UNSET,
    connector_id: int | Unset = UNSET,
    type_: Get2Type | Unset = UNSET,
    period_type: Get2PeriodType | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> ApiErrorResponse | list[Transaction] | None:
    """Returns a list of transactions based on the query parameters.
    The query parameters can be used to filter the transactions.

    Args:
        transaction_pk (int | Unset): Database primary key of the transaction
        connector_id (int | Unset): ID of the connector
        type_ (Get2Type | Unset): Return active or all transactions? Defaults to ALL
        period_type (Get2PeriodType | Unset): Return the time period of the transactions. If
            FROM_TO, 'from' and 'to' must be set. Additionally, 'to' must be after 'from'. Defaults to
            ALL
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
        ApiErrorResponse | list[Transaction]
    """

    return (
        await asyncio_detailed(
            client=client,
            transaction_pk=transaction_pk,
            connector_id=connector_id,
            type_=type_,
            period_type=period_type,
            charge_box_id=charge_box_id,
            ocpp_id_tag=ocpp_id_tag,
            user_id=user_id,
            from_=from_,
            to=to,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.get_blocked import GetBlocked
from ...models.get_expired import GetExpired
from ...models.get_in_transaction import GetInTransaction
from ...models.get_user_filter import GetUserFilter
from ...models.ocpp_tag_overview import OcppTagOverview
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ocpp_tag_pk: int | Unset = UNSET,
    id_tag: str | Unset = UNSET,
    parent_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    expired: GetExpired | Unset = UNSET,
    in_transaction: GetInTransaction | Unset = UNSET,
    blocked: GetBlocked | Unset = UNSET,
    note: str | Unset = UNSET,
    user_filter: GetUserFilter | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ocppTagPk"] = ocpp_tag_pk

    params["idTag"] = id_tag

    params["parentIdTag"] = parent_id_tag

    params["userId"] = user_id

    json_expired: str | Unset = UNSET
    if not isinstance(expired, Unset):
        json_expired = expired

    params["expired"] = json_expired

    json_in_transaction: str | Unset = UNSET
    if not isinstance(in_transaction, Unset):
        json_in_transaction = in_transaction

    params["inTransaction"] = json_in_transaction

    json_blocked: str | Unset = UNSET
    if not isinstance(blocked, Unset):
        json_blocked = blocked

    params["blocked"] = json_blocked

    params["note"] = note

    json_user_filter: str | Unset = UNSET
    if not isinstance(user_filter, Unset):
        json_user_filter = user_filter

    params["userFilter"] = json_user_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/ocppTags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiErrorResponse | list[OcppTagOverview] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OcppTagOverview.from_dict(response_200_item_data)

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
) -> Response[ApiErrorResponse | list[OcppTagOverview]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_pk: int | Unset = UNSET,
    id_tag: str | Unset = UNSET,
    parent_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    expired: GetExpired | Unset = UNSET,
    in_transaction: GetInTransaction | Unset = UNSET,
    blocked: GetBlocked | Unset = UNSET,
    note: str | Unset = UNSET,
    user_filter: GetUserFilter | Unset = UNSET,
) -> Response[ApiErrorResponse | list[OcppTagOverview]]:
    """Returns a list of Ocpp Tags based on the query parameters.
    The query parameters can be used to filter the Ocpp Tags.

    Args:
        ocpp_tag_pk (int | Unset): Database primary key of the OCPP tag
        id_tag (str | Unset): The OCPP tag
        parent_id_tag (str | Unset): The parent OCPP tag of this OCPP tag
        user_id (int | Unset): The User ID
        expired (GetExpired | Unset): Return expired, not expired, or all Ocpp tags? Defaults to
            ALL
        in_transaction (GetInTransaction | Unset): Return in-transaction, not in-transaction, or
            all Ocpp tags? Defaults to ALL
        blocked (GetBlocked | Unset): Return blocked, not blocked, or all Ocpp tags? Defaults to
            ALL
        note (str | Unset): Query by the note associated with the OCPP tag. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        user_filter (GetUserFilter | Unset): Filter by whether the OCPP tag is associated with a
            user or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | list[OcppTagOverview]]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
        id_tag=id_tag,
        parent_id_tag=parent_id_tag,
        user_id=user_id,
        expired=expired,
        in_transaction=in_transaction,
        blocked=blocked,
        note=note,
        user_filter=user_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_pk: int | Unset = UNSET,
    id_tag: str | Unset = UNSET,
    parent_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    expired: GetExpired | Unset = UNSET,
    in_transaction: GetInTransaction | Unset = UNSET,
    blocked: GetBlocked | Unset = UNSET,
    note: str | Unset = UNSET,
    user_filter: GetUserFilter | Unset = UNSET,
) -> ApiErrorResponse | list[OcppTagOverview] | None:
    """Returns a list of Ocpp Tags based on the query parameters.
    The query parameters can be used to filter the Ocpp Tags.

    Args:
        ocpp_tag_pk (int | Unset): Database primary key of the OCPP tag
        id_tag (str | Unset): The OCPP tag
        parent_id_tag (str | Unset): The parent OCPP tag of this OCPP tag
        user_id (int | Unset): The User ID
        expired (GetExpired | Unset): Return expired, not expired, or all Ocpp tags? Defaults to
            ALL
        in_transaction (GetInTransaction | Unset): Return in-transaction, not in-transaction, or
            all Ocpp tags? Defaults to ALL
        blocked (GetBlocked | Unset): Return blocked, not blocked, or all Ocpp tags? Defaults to
            ALL
        note (str | Unset): Query by the note associated with the OCPP tag. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        user_filter (GetUserFilter | Unset): Filter by whether the OCPP tag is associated with a
            user or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | list[OcppTagOverview]
    """

    return sync_detailed(
        client=client,
        ocpp_tag_pk=ocpp_tag_pk,
        id_tag=id_tag,
        parent_id_tag=parent_id_tag,
        user_id=user_id,
        expired=expired,
        in_transaction=in_transaction,
        blocked=blocked,
        note=note,
        user_filter=user_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_pk: int | Unset = UNSET,
    id_tag: str | Unset = UNSET,
    parent_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    expired: GetExpired | Unset = UNSET,
    in_transaction: GetInTransaction | Unset = UNSET,
    blocked: GetBlocked | Unset = UNSET,
    note: str | Unset = UNSET,
    user_filter: GetUserFilter | Unset = UNSET,
) -> Response[ApiErrorResponse | list[OcppTagOverview]]:
    """Returns a list of Ocpp Tags based on the query parameters.
    The query parameters can be used to filter the Ocpp Tags.

    Args:
        ocpp_tag_pk (int | Unset): Database primary key of the OCPP tag
        id_tag (str | Unset): The OCPP tag
        parent_id_tag (str | Unset): The parent OCPP tag of this OCPP tag
        user_id (int | Unset): The User ID
        expired (GetExpired | Unset): Return expired, not expired, or all Ocpp tags? Defaults to
            ALL
        in_transaction (GetInTransaction | Unset): Return in-transaction, not in-transaction, or
            all Ocpp tags? Defaults to ALL
        blocked (GetBlocked | Unset): Return blocked, not blocked, or all Ocpp tags? Defaults to
            ALL
        note (str | Unset): Query by the note associated with the OCPP tag. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        user_filter (GetUserFilter | Unset): Filter by whether the OCPP tag is associated with a
            user or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | list[OcppTagOverview]]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
        id_tag=id_tag,
        parent_id_tag=parent_id_tag,
        user_id=user_id,
        expired=expired,
        in_transaction=in_transaction,
        blocked=blocked,
        note=note,
        user_filter=user_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_pk: int | Unset = UNSET,
    id_tag: str | Unset = UNSET,
    parent_id_tag: str | Unset = UNSET,
    user_id: int | Unset = UNSET,
    expired: GetExpired | Unset = UNSET,
    in_transaction: GetInTransaction | Unset = UNSET,
    blocked: GetBlocked | Unset = UNSET,
    note: str | Unset = UNSET,
    user_filter: GetUserFilter | Unset = UNSET,
) -> ApiErrorResponse | list[OcppTagOverview] | None:
    """Returns a list of Ocpp Tags based on the query parameters.
    The query parameters can be used to filter the Ocpp Tags.

    Args:
        ocpp_tag_pk (int | Unset): Database primary key of the OCPP tag
        id_tag (str | Unset): The OCPP tag
        parent_id_tag (str | Unset): The parent OCPP tag of this OCPP tag
        user_id (int | Unset): The User ID
        expired (GetExpired | Unset): Return expired, not expired, or all Ocpp tags? Defaults to
            ALL
        in_transaction (GetInTransaction | Unset): Return in-transaction, not in-transaction, or
            all Ocpp tags? Defaults to ALL
        blocked (GetBlocked | Unset): Return blocked, not blocked, or all Ocpp tags? Defaults to
            ALL
        note (str | Unset): Query by the note associated with the OCPP tag. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        user_filter (GetUserFilter | Unset): Filter by whether the OCPP tag is associated with a
            user or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | list[OcppTagOverview]
    """

    return (
        await asyncio_detailed(
            client=client,
            ocpp_tag_pk=ocpp_tag_pk,
            id_tag=id_tag,
            parent_id_tag=parent_id_tag,
            user_id=user_id,
            expired=expired,
            in_transaction=in_transaction,
            blocked=blocked,
            note=note,
            user_filter=user_filter,
        )
    ).parsed

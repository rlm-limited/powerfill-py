from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_overview_1_ocpp_tag_filter import GetOverview1OcppTagFilter
from ...models.user_overview_list import UserOverviewList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_pk: int | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ocpp_tag_filter: GetOverview1OcppTagFilter | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userPk"] = user_pk

    params["ocppIdTag"] = ocpp_id_tag

    params["name"] = name

    params["email"] = email

    json_ocpp_tag_filter: str | Unset = UNSET
    if not isinstance(ocpp_tag_filter, Unset):
        json_ocpp_tag_filter = ocpp_tag_filter

    params["ocppTagFilter"] = json_ocpp_tag_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserOverviewList | None:
    if response.status_code == 200:
        response_200 = UserOverviewList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserOverviewList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_pk: int | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ocpp_tag_filter: GetOverview1OcppTagFilter | Unset = UNSET,
) -> Response[UserOverviewList]:
    """Returns a list of users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        user_pk (int | Unset): Should be exact match.
        ocpp_id_tag (str | Unset): Can be exact or substring match: any ocppIdTag containing the
            given string will be returned.
        name (str | Unset): Can be exact or substring match: any name containing the given string
            will be returned.
            Moreover, the name input can be a combination of first and last name.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        ocpp_tag_filter (GetOverview1OcppTagFilter | Unset): Filter by whether the user has OCPP
            tags or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserOverviewList]
    """

    kwargs = _get_kwargs(
        user_pk=user_pk,
        ocpp_id_tag=ocpp_id_tag,
        name=name,
        email=email,
        ocpp_tag_filter=ocpp_tag_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_pk: int | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ocpp_tag_filter: GetOverview1OcppTagFilter | Unset = UNSET,
) -> UserOverviewList | None:
    """Returns a list of users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        user_pk (int | Unset): Should be exact match.
        ocpp_id_tag (str | Unset): Can be exact or substring match: any ocppIdTag containing the
            given string will be returned.
        name (str | Unset): Can be exact or substring match: any name containing the given string
            will be returned.
            Moreover, the name input can be a combination of first and last name.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        ocpp_tag_filter (GetOverview1OcppTagFilter | Unset): Filter by whether the user has OCPP
            tags or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserOverviewList
    """

    return sync_detailed(
        client=client,
        user_pk=user_pk,
        ocpp_id_tag=ocpp_id_tag,
        name=name,
        email=email,
        ocpp_tag_filter=ocpp_tag_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_pk: int | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ocpp_tag_filter: GetOverview1OcppTagFilter | Unset = UNSET,
) -> Response[UserOverviewList]:
    """Returns a list of users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        user_pk (int | Unset): Should be exact match.
        ocpp_id_tag (str | Unset): Can be exact or substring match: any ocppIdTag containing the
            given string will be returned.
        name (str | Unset): Can be exact or substring match: any name containing the given string
            will be returned.
            Moreover, the name input can be a combination of first and last name.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        ocpp_tag_filter (GetOverview1OcppTagFilter | Unset): Filter by whether the user has OCPP
            tags or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserOverviewList]
    """

    kwargs = _get_kwargs(
        user_pk=user_pk,
        ocpp_id_tag=ocpp_id_tag,
        name=name,
        email=email,
        ocpp_tag_filter=ocpp_tag_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_pk: int | Unset = UNSET,
    ocpp_id_tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
    email: str | Unset = UNSET,
    ocpp_tag_filter: GetOverview1OcppTagFilter | Unset = UNSET,
) -> UserOverviewList | None:
    """Returns a list of users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        user_pk (int | Unset): Should be exact match.
        ocpp_id_tag (str | Unset): Can be exact or substring match: any ocppIdTag containing the
            given string will be returned.
        name (str | Unset): Can be exact or substring match: any name containing the given string
            will be returned.
            Moreover, the name input can be a combination of first and last name.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        ocpp_tag_filter (GetOverview1OcppTagFilter | Unset): Filter by whether the user has OCPP
            tags or not. Defaults to All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserOverviewList
    """

    return (
        await asyncio_detailed(
            client=client,
            user_pk=user_pk,
            ocpp_id_tag=ocpp_id_tag,
            name=name,
            email=email,
            ocpp_tag_filter=ocpp_tag_filter,
        )
    ).parsed

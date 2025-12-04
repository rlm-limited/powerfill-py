from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_user_dto_list import WebUserDtoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    web_user_pk: int | Unset = UNSET,
    email: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["webUserPk"] = web_user_pk

    params["email"] = email

    params["enabled"] = enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webUsers",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebUserDtoList | None:
    if response.status_code == 200:
        response_200 = WebUserDtoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebUserDtoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    web_user_pk: int | Unset = UNSET,
    email: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[WebUserDtoList]:
    """Returns a list of web users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        web_user_pk (int | Unset): Should be exact match.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        enabled (bool | Unset): Filter by the status. Defaults to null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebUserDtoList]
    """

    kwargs = _get_kwargs(
        web_user_pk=web_user_pk,
        email=email,
        enabled=enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    web_user_pk: int | Unset = UNSET,
    email: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> WebUserDtoList | None:
    """Returns a list of web users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        web_user_pk (int | Unset): Should be exact match.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        enabled (bool | Unset): Filter by the status. Defaults to null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebUserDtoList
    """

    return sync_detailed(
        client=client,
        web_user_pk=web_user_pk,
        email=email,
        enabled=enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    web_user_pk: int | Unset = UNSET,
    email: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> Response[WebUserDtoList]:
    """Returns a list of web users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        web_user_pk (int | Unset): Should be exact match.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        enabled (bool | Unset): Filter by the status. Defaults to null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebUserDtoList]
    """

    kwargs = _get_kwargs(
        web_user_pk=web_user_pk,
        email=email,
        enabled=enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    web_user_pk: int | Unset = UNSET,
    email: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
) -> WebUserDtoList | None:
    """Returns a list of web users based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        web_user_pk (int | Unset): Should be exact match.
        email (str | Unset): Can be exact or substring match: any email containing the given
            string will be returned.
        enabled (bool | Unset): Filter by the status. Defaults to null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebUserDtoList
    """

    return (
        await asyncio_detailed(
            client=client,
            web_user_pk=web_user_pk,
            email=email,
            enabled=enabled,
        )
    ).parsed

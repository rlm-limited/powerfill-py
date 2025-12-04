from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission_dto_for_user_list import PermissionDtoForUserList
from ...types import UNSET, Response


def _get_kwargs(
    *,
    user_pks: list[int],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_pks = user_pks

    params["userPks"] = json_user_pks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/permissions/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PermissionDtoForUserList | None:
    if response.status_code == 200:
        response_200 = PermissionDtoForUserList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PermissionDtoForUserList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_pks: list[int],
) -> Response[PermissionDtoForUserList]:
    """Retrieves the permissions for Ocpp Tags of given users.

    Args:
        user_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForUserList]
    """

    kwargs = _get_kwargs(
        user_pks=user_pks,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_pks: list[int],
) -> PermissionDtoForUserList | None:
    """Retrieves the permissions for Ocpp Tags of given users.

    Args:
        user_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForUserList
    """

    return sync_detailed(
        client=client,
        user_pks=user_pks,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_pks: list[int],
) -> Response[PermissionDtoForUserList]:
    """Retrieves the permissions for Ocpp Tags of given users.

    Args:
        user_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForUserList]
    """

    kwargs = _get_kwargs(
        user_pks=user_pks,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_pks: list[int],
) -> PermissionDtoForUserList | None:
    """Retrieves the permissions for Ocpp Tags of given users.

    Args:
        user_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            user_pks=user_pks,
        )
    ).parsed

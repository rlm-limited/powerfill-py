from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission_dto_for_tag import PermissionDtoForTag
from ...types import Response


def _get_kwargs(
    ocpp_tag_pk: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/permissions/ocppTags/{ocpp_tag_pk}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PermissionDtoForTag | None:
    if response.status_code == 200:
        response_200 = PermissionDtoForTag.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PermissionDtoForTag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PermissionDtoForTag]:
    """Retrieves the permissions for the given Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForTag]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> PermissionDtoForTag | None:
    """Retrieves the permissions for the given Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForTag
    """

    return sync_detailed(
        ocpp_tag_pk=ocpp_tag_pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PermissionDtoForTag]:
    """Retrieves the permissions for the given Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForTag]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> PermissionDtoForTag | None:
    """Retrieves the permissions for the given Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForTag
    """

    return (
        await asyncio_detailed(
            ocpp_tag_pk=ocpp_tag_pk,
            client=client,
        )
    ).parsed

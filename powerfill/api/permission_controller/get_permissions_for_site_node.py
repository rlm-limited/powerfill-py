from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission_dto_for_node import PermissionDtoForNode
from ...types import Response


def _get_kwargs(
    site_id: int,
    node_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/permissions/sites/{site_id}/node/{node_id}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PermissionDtoForNode | None:
    if response.status_code == 200:
        response_200 = PermissionDtoForNode.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PermissionDtoForNode]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PermissionDtoForNode]:
    """Retrieves the Ocpp Tag and Ocpp Tag group permissions at the given site node.

    Args:
        site_id (int):
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForNode]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> PermissionDtoForNode | None:
    """Retrieves the Ocpp Tag and Ocpp Tag group permissions at the given site node.

    Args:
        site_id (int):
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForNode
    """

    return sync_detailed(
        site_id=site_id,
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    site_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PermissionDtoForNode]:
    """Retrieves the Ocpp Tag and Ocpp Tag group permissions at the given site node.

    Args:
        site_id (int):
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForNode]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> PermissionDtoForNode | None:
    """Retrieves the Ocpp Tag and Ocpp Tag group permissions at the given site node.

    Args:
        site_id (int):
        node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForNode
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            node_id=node_id,
            client=client,
        )
    ).parsed

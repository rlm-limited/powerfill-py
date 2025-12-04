from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node import Node
from ...models.site_dto import SiteDto
from ...types import Response


def _get_kwargs(
    id: int,
    node_id: int,
    *,
    body: Node,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/sites/{id}/node/{node_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SiteDto | None:
    if response.status_code == 200:
        response_200 = SiteDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SiteDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: Node,
) -> Response[SiteDto]:
    """Adds a new node from the request payload to the site with <code>id</code> as a direct child under
    the parent node with <code>nodeId</code>.
    This new node can have its own children and charge boxes associated with it (and hence, can be seen
    as a subtree).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        body (Node):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: Node,
) -> SiteDto | None:
    """Adds a new node from the request payload to the site with <code>id</code> as a direct child under
    the parent node with <code>nodeId</code>.
    This new node can have its own children and charge boxes associated with it (and hence, can be seen
    as a subtree).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        body (Node):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDto
    """

    return sync_detailed(
        id=id,
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: Node,
) -> Response[SiteDto]:
    """Adds a new node from the request payload to the site with <code>id</code> as a direct child under
    the parent node with <code>nodeId</code>.
    This new node can have its own children and charge boxes associated with it (and hence, can be seen
    as a subtree).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        body (Node):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: Node,
) -> SiteDto | None:
    """Adds a new node from the request payload to the site with <code>id</code> as a direct child under
    the parent node with <code>nodeId</code>.
    This new node can have its own children and charge boxes associated with it (and hence, can be seen
    as a subtree).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        body (Node):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDto
    """

    return (
        await asyncio_detailed(
            id=id,
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed

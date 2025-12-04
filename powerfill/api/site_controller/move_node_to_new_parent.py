from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_dto import SiteDto
from ...types import Response


def _get_kwargs(
    id: int,
    node_id: int,
    new_parent_node_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/sites/{id}/node/{node_id}/move/{new_parent_node_id}",
    }

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
    new_parent_node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SiteDto]:
    """Moves the node with <code>nodeId</code> in site with <code>id</code> as a direct child under the
    parent node with <code>newParentNodeId</code>.
    Moving a node will also move all its children to the new parent.
    Therefore, this operation can be seen as a 'subtree move'.
    All charge boxes and permissions associated with the node will remain associated with it after the
    move.
    However, the permission inheritance will be different: the node will now inherit permissions from
    the new parent node instead of the old one (see <code>appliesToAllChildren</code> of permission
    APIs).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        new_parent_node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        new_parent_node_id=new_parent_node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    node_id: int,
    new_parent_node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> SiteDto | None:
    """Moves the node with <code>nodeId</code> in site with <code>id</code> as a direct child under the
    parent node with <code>newParentNodeId</code>.
    Moving a node will also move all its children to the new parent.
    Therefore, this operation can be seen as a 'subtree move'.
    All charge boxes and permissions associated with the node will remain associated with it after the
    move.
    However, the permission inheritance will be different: the node will now inherit permissions from
    the new parent node instead of the old one (see <code>appliesToAllChildren</code> of permission
    APIs).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        new_parent_node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDto
    """

    return sync_detailed(
        id=id,
        node_id=node_id,
        new_parent_node_id=new_parent_node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    node_id: int,
    new_parent_node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[SiteDto]:
    """Moves the node with <code>nodeId</code> in site with <code>id</code> as a direct child under the
    parent node with <code>newParentNodeId</code>.
    Moving a node will also move all its children to the new parent.
    Therefore, this operation can be seen as a 'subtree move'.
    All charge boxes and permissions associated with the node will remain associated with it after the
    move.
    However, the permission inheritance will be different: the node will now inherit permissions from
    the new parent node instead of the old one (see <code>appliesToAllChildren</code> of permission
    APIs).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        new_parent_node_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        new_parent_node_id=new_parent_node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    node_id: int,
    new_parent_node_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> SiteDto | None:
    """Moves the node with <code>nodeId</code> in site with <code>id</code> as a direct child under the
    parent node with <code>newParentNodeId</code>.
    Moving a node will also move all its children to the new parent.
    Therefore, this operation can be seen as a 'subtree move'.
    All charge boxes and permissions associated with the node will remain associated with it after the
    move.
    However, the permission inheritance will be different: the node will now inherit permissions from
    the new parent node instead of the old one (see <code>appliesToAllChildren</code> of permission
    APIs).
    The call returns the updated site structure.

    Args:
        id (int):
        node_id (int):
        new_parent_node_id (int):

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
            new_parent_node_id=new_parent_node_id,
            client=client,
        )
    ).parsed

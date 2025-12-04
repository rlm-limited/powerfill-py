from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_dto import SiteDto
from ...types import Response


def _get_kwargs(
    *,
    body: SiteDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sites",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SiteDto | None:
    if response.status_code == 201:
        response_201 = SiteDto.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: SiteDto,
) -> Response[SiteDto]:
    """Creates a new site with the given structure.
    The request payload should contain general information about the site and a flexible tree structure
    at 'structure' that models the real-world arrangement of this site.
    It can contain multiple, hierarchical levels and nodes within the tree (see 'children').
    Charge boxes can be associated with each node.

    Args:
        body (SiteDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SiteDto,
) -> SiteDto | None:
    """Creates a new site with the given structure.
    The request payload should contain general information about the site and a flexible tree structure
    at 'structure' that models the real-world arrangement of this site.
    It can contain multiple, hierarchical levels and nodes within the tree (see 'children').
    Charge boxes can be associated with each node.

    Args:
        body (SiteDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SiteDto,
) -> Response[SiteDto]:
    """Creates a new site with the given structure.
    The request payload should contain general information about the site and a flexible tree structure
    at 'structure' that models the real-world arrangement of this site.
    It can contain multiple, hierarchical levels and nodes within the tree (see 'children').
    Charge boxes can be associated with each node.

    Args:
        body (SiteDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SiteDto,
) -> SiteDto | None:
    """Creates a new site with the given structure.
    The request payload should contain general information about the site and a flexible tree structure
    at 'structure' that models the real-world arrangement of this site.
    It can contain multiple, hierarchical levels and nodes within the tree (see 'children').
    Charge boxes can be associated with each node.

    Args:
        body (SiteDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

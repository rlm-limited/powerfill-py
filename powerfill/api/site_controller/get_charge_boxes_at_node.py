from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_box_pk_list_dto import ChargeBoxPkListDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    node_id: int,
    *,
    include_all_children: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeAllChildren"] = include_all_children

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/sites/{id}/node/{node_id}/chargePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChargeBoxPkListDto | None:
    if response.status_code == 200:
        response_200 = ChargeBoxPkListDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChargeBoxPkListDto]:
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
    include_all_children: bool | Unset = False,
) -> Response[ChargeBoxPkListDto]:
    """Returns the charge boxes associated with the specified <code>nodeId</code>.

    Args:
        id (int):
        node_id (int):
        include_all_children (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargeBoxPkListDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        include_all_children=include_all_children,
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
    include_all_children: bool | Unset = False,
) -> ChargeBoxPkListDto | None:
    """Returns the charge boxes associated with the specified <code>nodeId</code>.

    Args:
        id (int):
        node_id (int):
        include_all_children (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargeBoxPkListDto
    """

    return sync_detailed(
        id=id,
        node_id=node_id,
        client=client,
        include_all_children=include_all_children,
    ).parsed


async def asyncio_detailed(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    include_all_children: bool | Unset = False,
) -> Response[ChargeBoxPkListDto]:
    """Returns the charge boxes associated with the specified <code>nodeId</code>.

    Args:
        id (int):
        node_id (int):
        include_all_children (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargeBoxPkListDto]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        include_all_children=include_all_children,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    include_all_children: bool | Unset = False,
) -> ChargeBoxPkListDto | None:
    """Returns the charge boxes associated with the specified <code>nodeId</code>.

    Args:
        id (int):
        node_id (int):
        include_all_children (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargeBoxPkListDto
    """

    return (
        await asyncio_detailed(
            id=id,
            node_id=node_id,
            client=client,
            include_all_children=include_all_children,
        )
    ).parsed

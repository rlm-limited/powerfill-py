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
    body: ChargeBoxPkListDto,
    remove_existing_associations: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["removeExistingAssociations"] = remove_existing_associations

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/sites/{id}/node/{node_id}/chargePoints/add",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: ChargeBoxPkListDto,
    remove_existing_associations: bool | Unset = False,
) -> Response[Any]:
    """Associates charge boxes with their PKs at the specified <code>nodeId</code>.
    The charge boxes and the site tree structure have to exist beforehand.

    Args:
        id (int):
        node_id (int):
        remove_existing_associations (bool | Unset):  Default: False.
        body (ChargeBoxPkListDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        body=body,
        remove_existing_associations=remove_existing_associations,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargeBoxPkListDto,
    remove_existing_associations: bool | Unset = False,
) -> Response[Any]:
    """Associates charge boxes with their PKs at the specified <code>nodeId</code>.
    The charge boxes and the site tree structure have to exist beforehand.

    Args:
        id (int):
        node_id (int):
        remove_existing_associations (bool | Unset):  Default: False.
        body (ChargeBoxPkListDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        node_id=node_id,
        body=body,
        remove_existing_associations=remove_existing_associations,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

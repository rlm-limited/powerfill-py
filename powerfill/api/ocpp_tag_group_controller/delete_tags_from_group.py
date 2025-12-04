from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ocpp_tag_id_list_dto import OcppTagIdListDto
from ...types import Response


def _get_kwargs(
    ocpp_tag_group_pk: int,
    *,
    body: OcppTagIdListDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/ocppTagGroups/{ocpp_tag_group_pk}/ocppTags/delete",
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
    ocpp_tag_group_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: OcppTagIdListDto,
) -> Response[Any]:
    """Deletes the given Ocpp Tags from the respective Ocpp Tag group.

    Args:
        ocpp_tag_group_pk (int):
        body (OcppTagIdListDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ocpp_tag_group_pk=ocpp_tag_group_pk,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ocpp_tag_group_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: OcppTagIdListDto,
) -> Response[Any]:
    """Deletes the given Ocpp Tags from the respective Ocpp Tag group.

    Args:
        ocpp_tag_group_pk (int):
        body (OcppTagIdListDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ocpp_tag_group_pk=ocpp_tag_group_pk,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

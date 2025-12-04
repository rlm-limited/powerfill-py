from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permission_dto_for_tag_group_list import PermissionDtoForTagGroupList
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ocpp_tag_group_pks: list[int],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ocpp_tag_group_pks = ocpp_tag_group_pks

    params["ocppTagGroupPks"] = json_ocpp_tag_group_pks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/permissions/ocppTagGroups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PermissionDtoForTagGroupList | None:
    if response.status_code == 200:
        response_200 = PermissionDtoForTagGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PermissionDtoForTagGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_group_pks: list[int],
) -> Response[PermissionDtoForTagGroupList]:
    """Retrieves the permissions for given Ocpp Tag groups.

    Args:
        ocpp_tag_group_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForTagGroupList]
    """

    kwargs = _get_kwargs(
        ocpp_tag_group_pks=ocpp_tag_group_pks,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_group_pks: list[int],
) -> PermissionDtoForTagGroupList | None:
    """Retrieves the permissions for given Ocpp Tag groups.

    Args:
        ocpp_tag_group_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForTagGroupList
    """

    return sync_detailed(
        client=client,
        ocpp_tag_group_pks=ocpp_tag_group_pks,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_group_pks: list[int],
) -> Response[PermissionDtoForTagGroupList]:
    """Retrieves the permissions for given Ocpp Tag groups.

    Args:
        ocpp_tag_group_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PermissionDtoForTagGroupList]
    """

    kwargs = _get_kwargs(
        ocpp_tag_group_pks=ocpp_tag_group_pks,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ocpp_tag_group_pks: list[int],
) -> PermissionDtoForTagGroupList | None:
    """Retrieves the permissions for given Ocpp Tag groups.

    Args:
        ocpp_tag_group_pks (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PermissionDtoForTagGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            ocpp_tag_group_pks=ocpp_tag_group_pks,
        )
    ).parsed

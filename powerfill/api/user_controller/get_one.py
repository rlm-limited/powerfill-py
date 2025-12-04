from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_form import UserForm
from ...types import Response


def _get_kwargs(
    user_pk: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_pk}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserForm | None:
    if response.status_code == 200:
        response_200 = UserForm.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserForm]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[UserForm]:
    """Returns a single user based on the userPk.

    Args:
        user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserForm]
    """

    kwargs = _get_kwargs(
        user_pk=user_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> UserForm | None:
    """Returns a single user based on the userPk.

    Args:
        user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserForm
    """

    return sync_detailed(
        user_pk=user_pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[UserForm]:
    """Returns a single user based on the userPk.

    Args:
        user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserForm]
    """

    kwargs = _get_kwargs(
        user_pk=user_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> UserForm | None:
    """Returns a single user based on the userPk.

    Args:
        user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserForm
    """

    return (
        await asyncio_detailed(
            user_pk=user_pk,
            client=client,
        )
    ).parsed

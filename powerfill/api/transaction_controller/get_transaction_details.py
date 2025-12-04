from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction_details import TransactionDetails
from ...types import Response


def _get_kwargs(
    transaction_pk: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/transactions/{transaction_pk}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TransactionDetails | None:
    if response.status_code == 200:
        response_200 = TransactionDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TransactionDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[TransactionDetails]:
    """Returns the details of a single transaction based on the transactionPk.
    The details are the intermediate values of the transaction.

    Args:
        transaction_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionDetails]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> TransactionDetails | None:
    """Returns the details of a single transaction based on the transactionPk.
    The details are the intermediate values of the transaction.

    Args:
        transaction_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionDetails
    """

    return sync_detailed(
        transaction_pk=transaction_pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[TransactionDetails]:
    """Returns the details of a single transaction based on the transactionPk.
    The details are the intermediate values of the transaction.

    Args:
        transaction_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionDetails]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> TransactionDetails | None:
    """Returns the details of a single transaction based on the transactionPk.
    The details are the intermediate values of the transaction.

    Args:
        transaction_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionDetails
    """

    return (
        await asyncio_detailed(
            transaction_pk=transaction_pk,
            client=client,
        )
    ).parsed

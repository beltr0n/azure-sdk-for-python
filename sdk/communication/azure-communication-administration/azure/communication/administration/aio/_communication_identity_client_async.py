# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from azure.core.tracing.decorator_async import distributed_trace_async

from .._identity._generated.aio._communication_identity_client\
    import CommunicationIdentityClient as CommunicationIdentityClientGen
from .._identity._generated.models import CommunicationIdentityAccessToken

from .._shared.utils import parse_connection_str, get_authentication_policy
from .._shared.models import CommunicationUser
from .._version import SDK_MONIKER


class CommunicationIdentityClient:
    """Azure Communication Services Identity client.

    :param str endpoint:
        The endpoint url for Azure Communication Service resource.
    :param credential:
        The credentials with which to authenticate. The value is an account
        shared access key

    .. admonition:: Example:

        .. literalinclude:: ../../samples/identity_samples_async.py
            :language: python
            :dedent: 8
    """
    def __init__(
            self,
            endpoint, # type: str
            credential, # type: str
            **kwargs # type: Any
        ):
        # type: (...) -> None
        try:
            if not endpoint.lower().startswith('http'):
                endpoint = "https://" + endpoint
        except AttributeError:
            raise ValueError("Account URL must be a string.")

        if not credential:
            raise ValueError(
                "You need to provide account shared key to authenticate.")

        self._endpoint = endpoint
        self._identity_service_client = CommunicationIdentityClientGen(
            self._endpoint,
            authentication_policy=get_authentication_policy(endpoint, credential, is_async=True),
            sdk_moniker=SDK_MONIKER,
            **kwargs)

    @classmethod
    def from_connection_string(
            cls, conn_str,  # type: str
            **kwargs  # type: Any
        ):  # type: (...) -> CommunicationIdentityClient
        """Create CommunicationIdentityClient from a Connection String.

        :param str conn_str:
            A connection string to an Azure Communication Service resource.
        :returns: Instance of CommunicationIdentityClient.
        :rtype: ~azure.communication.aio.CommunicationIdentityClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/identity_samples.py
                :start-after: [START auth_from_connection_string]
                :end-before: [END auth_from_connection_string]
                :language: python
                :dedent: 8
                :caption: Creating the CommunicationIdentityClient from a connection string.
        """
        endpoint, access_key = parse_connection_str(conn_str)

        return cls(endpoint, access_key, **kwargs)

    @distributed_trace_async
    async def create_user(self, **kwargs):
        # type: (...) -> CommunicationUser
        """create a single Communication user

        :return: CommunicationUser
        :rtype: ~azure.communication.administration.CommunicationUser
        """
        return await self._identity_service_client.communication_identity.create_identity(
            cls=lambda pr, u, e: CommunicationUser(u.id),
            **kwargs)

    @distributed_trace_async
    async def create_user_with_token(
            self,
            scopes, # type: List[Union[str, "_model.CommunicationIdentityTokenScope"]]
            **kwargs
        ):
        # type: (...) -> Tuple[CommunicationUser, CommunicationIdentityAccessToken]
        """create a single Communication user along with an Identity Token

        :param scopes:
            List of scopes to be added to the token.
        :type scopes: list[str or 
            ~azure.communication.administration.models.CommunicationIdentityTokenScope]
        :return: A tuple of a CommunicationUser and a CommunicationIdentityAccessToken.
        :rtype: tuple of (~azure.communication.administration.CommunicationUser, ~azure.communication.administration.CommunicationIdentityAccessToken)
        """
        return await self._identity_service_client.communication_identity.create_identity(
            create_token_with_scopes=scopes,
            cls=lambda pr, u, e: CommunicationUser(u.id),
            **kwargs)
        pass

    @distributed_trace_async
    async def delete_user(
            self,
            communication_user, # type: CommunicationUser
            **kwargs # type: Any
        ):
        # type: (...) -> None
        """Triggers revocation event for user and deletes all its data.

        :param communication_user:
            Azure Communication User to delete
        :type communication_user: ~azure.communication.administration.CommunicationUser
        :return: None
        :rtype: None
        """
        await self._identity_service_client.communication_identity.delete_identity(
            communication_user.identifier, **kwargs)

    @distributed_trace_async
    async def issue_token(
            self,
            user, # type: CommunicationUser
            scopes, # type: List[Union[str, "_model.CommunicationIdentityTokenScope"]]
            **kwargs # type: Any
        ):
        # type: (...) -> CommunicationIdentityAccessToken
        """Generates a new token for an identity.

        :param user: Azure Communication User
        :type user: ~azure.communication.administration.CommunicationUser
        :param scopes:
            List of scopes to be added to the token.
        :type scopes: list[str or 
            ~azure.communication.administration.models.CommunicationIdentityTokenScope]
        :return: CommunicationIdentityAccessToken
        :rtype: ~azure.communication.administration.CommunicationIdentityAccessToken
        """
        return await self._identity_service_client.communication_identity.issue_access_token(
            user.identifier,
            scopes,
            **kwargs)

    @distributed_trace_async
    async def revoke_tokens(
            self,
            user, # type: CommunicationUser
            **kwargs # type: Any
        ):
        # type: (...) -> None
        """Schedule revocation of all tokens of an identity.

        :param user: Azure Communication User.
        :type user: ~azure.communication.administration.CommunicationUser
        :return: None
        :rtype: None
        """
        return await self._identity_service_client.communication_identity.revoke_access_tokens(
            user.identifier if user else None,
            **kwargs)

    async def __aenter__(self) -> "CommunicationIdentityClient":
        await self._identity_service_client.__aenter__()
        return self

    async def __aexit__(self, *args: "Any") -> None:
        await self.close()

    async def close(self) -> None:
        """Close the :class:
        `~azure.communication.administration.aio.CommunicationIdentityClient` session.
        """
        await self._identity_service_client.__aexit__()

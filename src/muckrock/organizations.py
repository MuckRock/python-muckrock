"""
Organizations
"""

# Standard Library
import logging

# Local
from .base import APIResults, BaseAPIClient, BaseAPIObject

logger = logging.getLogger("organizations")


class Organization(BaseAPIObject):
    """A single organization object."""

    api_path = "organizations"

    def __str__(self):
        return f"Organization {self.id} - Name: {self.name}"  # pylint:disable=no-member


class OrganizationClient(BaseAPIClient):
    """Client for interacting with organizations."""

    api_path = "organizations"
    resource = Organization

    def list(self, **params):
        """
        List all organizations with optional filtering.

        :param params: Query parameters to filter results (e.g., name, slug, individual).
        :return: APIResults containing Organization objects.
        """
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

    def retrieve(self, organization_id):
        """
        Retrieve a single organization by its ID.

        :param organization_id: The ID of the organization to retrieve.
        :return: An Organization object.
        """
        response = self.client.get(f"{self.api_path}/{organization_id}/")
        return Organization(self.client, response.json())

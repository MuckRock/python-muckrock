""" Jurisdiction handling requests """

import logging

from .base import APIResults, BaseAPIClient, BaseAPIObject

logger = logging.getLogger("muckrock")


class Jurisdiction(BaseAPIObject):
    """A single Jurisdiction object."""

    api_path = "jurisdictions"

    def __str__(self):
        return self.name  # pylint:disable=no-member


class JurisdictionClient(BaseAPIClient):
    """Client for interacting with Jurisdictions."""

    api_path = "jurisdictions"
    resource = Jurisdiction

    def list(self, **params):
        """
        List all jurisdictions with optional filtering.

        :param params: Query parameters to filter results (e.g., `level`, `parent`).
        :return: An APIResults object containing a list of Jurisdiction objects.
        """
        try:
            response = self.client.get(self.api_path, params=params)
            return APIResults(self.resource, self.client, response)
        except Exception as e:
            logger.error("Error retrieving jurisdictions list: %s", e)
            raise

    def retrieve(self, jurisdiction_id):
        """
        Retrieve a single jurisdiction by its ID.

        :param jurisdiction_id: The ID of the jurisdiction to retrieve.
        :return: A Jurisdiction object.
        """
        try:
            response = self.client.get(f"{self.api_path}/{jurisdiction_id}/")
            return Jurisdiction(self.client, response.json())
        except Exception as e:
            logger.error(
                "Error retrieving jurisdiction with ID %s: %s", jurisdiction_id, e
            )
            raise

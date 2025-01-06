# Standard Library
import logging

# Local
from .base import BaseAPIObject, BaseAPIClient, APIResults

logger = logging.getLogger("muckrock")


class Agency(BaseAPIObject):
    """A single agency object."""

    api_path = "agencies"

    def __str__(self):
        return self.name


class AgencyClient(BaseAPIClient):
    """Client for interacting with agency objects."""

    api_path = "agencies"
    resource = Agency

    def list(self, **params):
        """
        List all agencies with optional filtering.

        :param params: Query parameters to filter results (e.g., jurisdiction, types, status).
        :return: APIResults object containing the list of agencies.
        """
        if "types" in params and isinstance(params["types"], list):
            params["types"] = ",".join(params["types"])
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

    def retrieve(self, agency_id):
        """
        Retrieve a single agency by its ID.

        :param agency_id: The ID of the agency to retrieve.
        :return: An `Agency` object representing the agency.
        """
        response = self.client.get(f"{self.api_path}/{agency_id}/")
        return Agency(self.client, response.json())

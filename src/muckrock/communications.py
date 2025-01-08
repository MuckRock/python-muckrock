"""
Communications management for the Python-MuckRock library.
"""

# Standard Library
import logging

# Local
from .base import BaseAPIClient, BaseAPIObject, APIResults

logger = logging.getLogger("communications")


class Communication(BaseAPIObject):
    """A single FOIA communication object."""

    api_path = "communications"

    def __str__(self):
        return f"Communication {self.id}"


class CommunicationClient(BaseAPIClient):
    """Client for interacting with FOIA communications."""

    api_path = "communications"
    resource = Communication

    def list(self, **params):
        """
        List all FOIA communications with optional filtering.

        :param params: Query parameters to filter results (e.g., foia, from_user, subject).
        :return: APIResults containing Communication objects.
        """
        if "foia" in params and isinstance(params["foia"], list):
            params["foia"] = ",".join(map(str, params["foia"]))
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

    def retrieve(self, communication_id):
        """
        Retrieve a single FOIA communication by its ID.

        :param communication_id: The ID of the communication to retrieve.
        :return: A Communication object.
        """
        response = self.client.get(f"{self.api_path}/{communication_id}/")
        return Communication(self.client, response.json())

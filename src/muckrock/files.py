"""
Files 
"""

# Standard Library
import logging

# Local
from .base import APIResults, BaseAPIClient, BaseAPIObject

logger = logging.getLogger("files")


class File(BaseAPIObject):
    """A single FOIA file object."""

    api_path = "files"

    def __str__(self):
        return f"File {self.id} - Title: {self.title}"  # pylint:disable=no-member


class FileClient(BaseAPIClient):
    """Client for interacting with FOIA files."""

    api_path = "files"
    resource = File

    def list(self, **params):
        """
        List all FOIA files with optional filtering.

        :param params: Query parameters to filter results (e.g., title, source, pages).
        :return: APIResults containing FOIAFile objects.
        """
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

    def retrieve(self, file_id):
        """
        Retrieve a single FOIA file by its ID.

        :param file_id: The ID of the file to retrieve.
        :return: A FOIAFile object.
        """
        response = self.client.get(f"{self.api_path}/{file_id}/")
        return File(self.client, response.json())

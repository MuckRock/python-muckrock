"""
Projects
"""

# Standard Library
import logging

# Local
from .base import APIResults, BaseAPIClient, BaseAPIObject

logger = logging.getLogger("projects")


class Project(BaseAPIObject):
    """A single user object."""

    api_path = "projects"

    def __str__(self):
        return f"Project {self.id} - Title: {self.title}"  # pylint:disable=no-member


class ProjectClient(BaseAPIClient):
    """Client for interacting with users."""

    api_path = "projects"
    resource = Project

    def retrieve(self, project_id):
        """
        Retrieve a single project by its ID.

        :param project_id: The ID of the project to retrieve.
        :return: A project object.
        """
        response = self.client.get(f"{self.api_path}/{project_id}/")
        return Project(self.client, response.json())

    def list(self, **params):
        """
        List all projects with optional filtering.

        :param params: Query parameters to filter results
        :return: APIResults containing User objects.
        """
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

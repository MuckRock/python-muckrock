"""
Users
"""

# Standard Library
import logging

# Local
from .base import APIResults, BaseAPIClient, BaseAPIObject

logger = logging.getLogger("users")


class User(BaseAPIObject):
    """A single user object."""

    api_path = "users"

    def __str__(self):
        return f"User {self.id} - Username: {self.username}, Email: {self.email}"  # pylint:disable=no-member


class UserClient(BaseAPIClient):
    """Client for interacting with users."""

    api_path = "users"
    resource = User

    def me(self):
        """
        Retrieve the currently authenticated user.

        :return: A User object representing the authenticated user.
        """
        response = self.client.get(f"{self.api_path}/me/")
        return User(self.client, response.json())

    def retrieve(self, user_id):
        """
        Retrieve a single user by its ID.

        :param user_id: The ID of the user to retrieve.
        :return: A User object.
        """
        response = self.client.get(f"{self.api_path}/{user_id}/")
        return User(self.client, response.json())

    def list(self, **params):
        """
        List all users with optional filtering.

        :param params: Query parameters to filter results (e.g., username, email).
        :return: APIResults containing User objects.
        """
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

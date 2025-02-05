""" FOIA Request handling portion """

# Standard Library
import logging

from .base import APIResults, BaseAPIClient, BaseAPIObject
# Local
from .exceptions import APIError

logger = logging.getLogger("foia")
# logger.setLevel(logging.DEBUG)


class Request(BaseAPIObject):
    """A single FOIA request object."""

    api_path = "requests"

    def __str__(self):
        return self.title  # pylint:disable = no-member

    def get_communications(self):
        """
        Retrieve all communications related to this FOIA request.

        :return: APIResults containing Communication objects.
        """
        return self._client.communications.list(
            foia=self.id # pylint:disable=no-member
        )


class RequestClient(BaseAPIClient):
    """Client for interacting with FOIA requests."""

    api_path = "requests"
    resource = Request

    def list(self, **params):
        """
        List all FOIA requests with optional filtering.

        :param params: Query parameters to filter results (e.g., status, agency).
        """
        if "status" in params and isinstance(params["status"], list):
            params["status"] = ",".join(params["status"])
        response = self.client.get(self.api_path, params=params)
        return APIResults(self.resource, self.client, response)

    def retrieve(self, request_id):
        """
        Retrieve a single FOIA request by its ID.

        :param request_id: The ID of the request to retrieve.
        """
        response = self.client.get(f"{self.api_path}/{request_id}/")
        return Request(self.client, response.json())

    def create(
        self,
        title,
        requested_docs,
        organization,
        agencies,
        embargo_status="public",
        **kwargs,
    ):
        """Create a FOIA request."""
        if not isinstance(agencies, list) or not agencies:
            raise ValueError("Agencies must be a non-empty list of agency IDs.")

        payload = {
            "title": title,
            "requested_docs": requested_docs,
            "organization": organization,
            "agencies": agencies,
            "embargo_status": embargo_status,
            **kwargs,
        }

        obj_list = []
        try:
            response = self.client.post(
                f"{self.api_path}/#post-object-form", json=payload
            )
            response.raise_for_status()
            create_json = response.json()
            obj_list.extend(create_json)
            logger.debug("Object list after processing: %s", obj_list)
            full_url = f"https://www.muckrock.com{create_json['location']}"
            print(full_url)
            return full_url
        except APIError as exc:
            logger.error("Error creating requests: %s", str(exc))
            raise

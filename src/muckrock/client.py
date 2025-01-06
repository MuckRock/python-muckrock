# Standard Library
import logging

# Third Party
from squarelet import SquareletClient

# Local Imports
from .requests import RequestClient
from .jurisdictions import JurisdictionClient
from .agencies import AgencyClient
from .communications import CommunicationClient

logger = logging.getLogger("muckrock")

class MuckRock(SquareletClient):
    """
    The public interface for the MuckRock API, now integrated with SquareletClient
    """
    # pylint:disable=too-many-positional-arguments
    def __init__(
        self,
        username=None,
        password=None,
        base_uri="https://muckrock-staging.herokuapp.com/api_v2/", # Change to https://www.muckrock.com/api_v2/ when live
        auth_uri="https://squarelet-staging.herokuapp.com/api/", # Change to https://accounts.muckrock.com/api/ when live
        timeout=20,
        loglevel=None,
        rate_limit=True,
        rate_limit_sleep=True,
    ):
       # Initialize SquareletClient for authentication and request handling
        super().__init__(
            base_uri=base_uri,
            username=username,
            password=password,
            auth_uri=auth_uri,
            timeout=timeout,
            rate_limit=rate_limit,
            rate_limit_sleep=rate_limit_sleep
        )

        # Set up logging
        if loglevel:
            logging.basicConfig(
                level=loglevel,
                format="%(asctime)s %(levelname)-8s %(name)-25s %(message)s",
            )
        else:
            logger.addHandler(logging.NullHandler())

        self.requests = RequestClient(self)
        self.jurisdictions = JurisdictionClient(self)
        self.agencies = AgencyClient(self)
        self.communications = CommunicationClient(self)

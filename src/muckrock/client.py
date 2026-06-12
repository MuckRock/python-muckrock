"""
Provides the client wrapper with Squarelet
"""

# Standard Library
import logging
import time

# Third Party
import token_bucket
from squarelet import SquareletClient

from .agencies import AgencyClient
from .communications import CommunicationClient
from .files import FileClient
from .jurisdictions import JurisdictionClient
from .organizations import OrganizationClient
from .projects import ProjectClient

# Local Imports
from .requests import RequestClient
from .users import UserClient

logger = logging.getLogger("muckrock")

# Per-endpoint rate limits.
# Format: (url_pattern, rate_per_second, capacity)
#
# Endpoint          Rate        Burst   Notes
# --------          ----        -----   -----
# requests/          15/min      100
# communications/    15/min      100
# agencies/          15/min      100
# files/             15/min      100
# jurisdictions/     15/min      100
# projects/          15/min      100
# organizations/      5/min        5    Heavy rate limit, minimal burst
# users/              5/min        5    Heavy rate limit, minimal burst
ENDPOINT_RATE_LIMITS = [
    ("organizations/", 5 / 60, 5),
    ("users/", 5 / 60, 5),
    ("requests/", 15 / 60, 100),
    ("communications/", 15 / 60, 100),
    ("agencies/", 15 / 60, 100),
    ("files/", 15 / 60, 100),
    ("jurisdictions/", 15 / 60, 100),
    ("projects/", 15 / 60, 100),
]


class MuckRock(SquareletClient): # pylint:disable=too-many-instance-attributes
    """
    The public interface for the MuckRock API, now integrated with SquareletClient
    """

    # pylint:disable=too-many-positional-arguments, too-many-arguments
    def __init__(
        self,
        username=None,
        password=None,
        base_uri="https://www.muckrock.com/api_v2/",
        auth_uri="https://accounts.muckrock.com/api/",
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
            rate_limit_sleep=rate_limit_sleep,
        )

        # Set up logging
        if loglevel:
            logging.basicConfig(
                level=loglevel,
                format="%(asctime)s %(levelname)-8s %(name)-25s %(message)s",
            )
        else:
            logger.addHandler(logging.NullHandler())

        # Build per-endpoint token bucket rate limiters
        storage = token_bucket.MemoryStorage()
        self._endpoint_limiters = [
            (
                pattern,
                token_bucket.Limiter(rate=rate, capacity=capacity, storage=storage),
                pattern,
            )
            for pattern, rate, capacity in ENDPOINT_RATE_LIMITS
        ]

        self.requests = RequestClient(self)
        self.jurisdictions = JurisdictionClient(self)
        self.agencies = AgencyClient(self)
        self.communications = CommunicationClient(self)
        self.files = FileClient(self)
        self.organizations = OrganizationClient(self)
        self.users = UserClient(self)
        self.projects = ProjectClient(self)

    def _base_request(
        self, method, url, raise_error=True, **kwargs
    ):  # pylint: disable=unused-argument
        return super().request(method, url, raise_error=raise_error, **kwargs)

    def request(self, method, url, raise_error=True, **kwargs):
        for pattern, limiter, bucket_key in self._endpoint_limiters:
            if pattern in url:
                while not limiter.consume(bucket_key):
                    time.sleep(0.1)
                return self._base_request(
                    method, url, raise_error=raise_error, **kwargs
                )
        return super().request(method, url, raise_error=raise_error, **kwargs)

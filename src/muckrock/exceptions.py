"""
Custom exceptions for python-muckrock
"""

# pylint: disable=unused-import
# Import exceptions from python-squarelet
from squarelet.exceptions import (APIError, CredentialsFailedError,
                                  DoesNotExistError, DuplicateObjectError,
                                  MultipleObjectsReturnedError)
from squarelet.exceptions import SquareletError as MuckRockError

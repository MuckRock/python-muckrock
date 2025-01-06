"""
Custom exceptions for python-muckrock
"""

# pylint: disable=unused-import
# Import exceptions from python-squarelet
from squarelet.exceptions import SquareletError as MuckRockError
from squarelet.exceptions import DuplicateObjectError
from squarelet.exceptions import CredentialsFailedError
from squarelet.exceptions import APIError
from squarelet.exceptions import DoesNotExistError
from squarelet.exceptions import MultipleObjectsReturnedError

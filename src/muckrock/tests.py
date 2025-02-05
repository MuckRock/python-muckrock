""" Tests the functions for this Python wrapper of the v2 of MuckRock API """

import os

import pytest
from squarelet.exceptions import DoesNotExistError
from muckrock import MuckRock



# pylint:disable=redefined-outer-name
@pytest.fixture
def muckrock_client():
    """Fixture to create a MuckRock client instance."""
    mr_user = os.environ.get("MR_USER")
    mr_password = os.environ.get("MR_PASSWORD")
    if not mr_user or not mr_password:
        pytest.skip("MR_USER and MR_PASSWORD environment variables are required.")
    return MuckRock(
        username=mr_user,
        password=mr_password,
    )


@pytest.fixture
def regular_user_client():
    """Fixture to create a MuckRock client with base permissions."""
    reg_user = os.environ.get("REG_USER")
    reg_password = os.environ.get("REG_PASSWORD")
    if not reg_user or not reg_password:
        pytest.skip("REG_USER and REG_PASSWORD environment variables are required.")
    return MuckRock(
        username=reg_user,
        password=reg_password,
    )


def test_list_agencies(muckrock_client):
    agencies = muckrock_client.agencies.list()
    assert agencies, "Expected a non-empty list of agencies."
    print(agencies)


def test_retrieve_agencies(muckrock_client):
    agency_id = 1
    agency = muckrock_client.agencies.retrieve(agency_id)
    assert agency.id == agency_id, f"Expected agency ID to be {agency_id}."
    print(agency)


def test_list_communications(muckrock_client):
    communications = muckrock_client.communications.list()
    assert communications, "Expected a non-empty list of communications."
    print(communications)


def test_retrieve_communications(muckrock_client):
    communication_id = 1
    communication = muckrock_client.communications.retrieve(communication_id)
    assert (
        communication.id == communication_id
    ), f"Expected communication ID to be {communication_id}."
    print(communication)


def test_list_files(muckrock_client):
    files = muckrock_client.files.list()
    assert files, "Expected a non-empty list of files."
    print(files)


def test_retrieve_files(muckrock_client):
    file_id = 1
    file = muckrock_client.files.retrieve(file_id)
    assert file.id == file_id, f"Expected file ID to be {file_id}."
    print(file)


def test_list_jurisdictions(muckrock_client):
    jurisdictions = muckrock_client.jurisdictions.list()
    assert jurisdictions, "Expected a non-empty list of jurisdictions."
    print(jurisdictions)


def test_retrieve_jurisdictions(muckrock_client):
    jurisdiction_id = 1
    jurisdiction = muckrock_client.jurisdictions.retrieve(jurisdiction_id)
    assert (
        jurisdiction.id == jurisdiction_id
    ), f"Expected jurisdiction ID to be {jurisdiction_id}."


def test_list_organizations(muckrock_client):
    organizations = muckrock_client.organizations.list()
    orgs_list = organizations.results
    assert len(orgs_list) > 5


def test_list_organizations_nonstaff(regular_user_client):
    organizations = regular_user_client.organizations.list()
    orgs_list = organizations.results
    assert len(orgs_list) == 1  # This test user is only part of one org


def test_retrieve_organizations(muckrock_client):
    organization_id = 1
    organization = muckrock_client.organizations.retrieve(organization_id)
    assert (
        organization.id == organization_id
    ), f"Expected organization ID to be {organization_id}."
    print(organization)


def test_retrieve_organizations_nonstaff(regular_user_client):
    organization_id = 1
    with pytest.raises(DoesNotExistError):
        regular_user_client.organizations.retrieve(organization_id)


def test_list_requests(muckrock_client):
    requests = muckrock_client.requests.list()
    assert requests, "Expected a non-empty list of requests."
    print(requests)


def test_retrieve_requests(muckrock_client):
    request_id = 17
    request = muckrock_client.requests.retrieve(request_id)
    assert request.id == request_id, f"Expected request ID to be {request_id}."
    print(request)


def test_retrieve_requests_nonstaff(regular_user_client):
    request_id = 86429
    with pytest.raises(DoesNotExistError):
        regular_user_client.requests.retrieve(request_id)


def test_create_requests(muckrock_client):
    new_request_data = {
        "title": "Test FOIA Request",
        "requested_docs": "This is a test FOIA request.",
        "organization": 1,
        "agencies": [248],  # This is the ID of a test agency
    }
    new_request = muckrock_client.requests.create(**new_request_data)
    assert "test-foia-request" in new_request


def test_list_users(muckrock_client):
    users = muckrock_client.users.list()
    user_list = users.results
    assert (
        len(user_list) > 1
    )  # Expect a list of users greater than 1 as it is staff perms


def test_list_users_non_staff(regular_user_client):
    users = regular_user_client.users.list()
    user_list = users.results
    assert len(user_list) == 1


def test_retrieve_users(muckrock_client):
    user_id = 1
    user = muckrock_client.users.retrieve(user_id)
    assert user.id == user_id, f"Expected user ID to be {user_id}."


def test_retrieve_users_nonstaff(regular_user_client):
    user_id = 1
    with pytest.raises(DoesNotExistError):
        regular_user_client.users.retrieve(user_id)

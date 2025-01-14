import os
import pytest
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
    assert communication.id == communication_id, f"Expected communication ID to be {communication_id}."
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
    assert jurisdiction.id == jurisdiction_id, f"Expected jurisdiction ID to be {jurisdiction_id}."
    print(jurisdiction)


def test_list_organizations(muckrock_client):
    organizations = muckrock_client.organizations.list()
    assert organizations, "Expected a non-empty list of organizations."
    print(organizations)


def test_retrieve_organizations(muckrock_client):
    organization_id = 1
    organization = muckrock_client.organizations.retrieve(organization_id)
    assert organization.id == organization_id, f"Expected organization ID to be {organization_id}."
    print(organization)


def test_list_requests(muckrock_client):
    requests = muckrock_client.requests.list()
    assert requests, "Expected a non-empty list of requests."
    print(requests)


def test_retrieve_requests(muckrock_client):
    request_id = 17
    request = muckrock_client.requests.retrieve(request_id)
    assert request.id == request_id, f"Expected request ID to be {request_id}."
    print(request)


def test_create_requests(muckrock_client):
    new_request_data = {
        "title": "Test FOIA Request",
        "requested_docs": "This is a test FOIA request.",
        "organization": 1,
        "agencies": [248], # This is the ID of a test agency
    }
    new_request = muckrock_client.requests.create(**new_request_data)
    assert "test-foia-request" in new_request

def test_list_users(muckrock_client):
    users = muckrock_client.users.list()
    assert users, "Expected a non-empty list of users."
    print(users)


def test_retrieve_users(muckrock_client):
    user_id = 1
    user = muckrock_client.users.retrieve(user_id)
    assert user.id == user_id, f"Expected user ID to be {user_id}."
    print(user)

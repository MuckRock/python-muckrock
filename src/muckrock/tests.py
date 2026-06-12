"""Tests the functions for this Python wrapper of the v2 of MuckRock API"""

# Standard Library
import os

# Third Party
import pytest
from muckrock import MuckRock


# pylint:disable=redefined-outer-name
@pytest.fixture
def client():
    """Fixture to create a MuckRock client instance."""
    username = os.environ.get("REG_USER")
    password = os.environ.get("REG_PASSWORD")
    if not username or not password:
        pytest.skip("REG_USER and REG_PASSWORD environment variables are required.")
    return MuckRock(username=username, password=password)


def test_list_agencies(client):
    agencies = client.agencies.list()
    assert agencies, "Expected a non-empty list of agencies."


def test_retrieve_agency(client):
    agency = client.agencies.retrieve(1)
    assert agency.id == 1


def test_list_communications(client):
    communications = client.communications.list()
    assert communications, "Expected a non-empty list of communications."


def test_retrieve_communication(client):
    communication = client.communications.retrieve(1)
    assert communication.id == 1


def test_list_files(client):
    files = client.files.list()
    assert files, "Expected a non-empty list of files."


def test_retrieve_file(client):
    file = client.files.retrieve(1)
    assert file.id == 1


def test_list_jurisdictions(client):
    jurisdictions = client.jurisdictions.list()
    assert jurisdictions, "Expected a non-empty list of jurisdictions."


def test_retrieve_jurisdiction(client):
    jurisdiction = client.jurisdictions.retrieve(1)
    assert jurisdiction.id == 1


def test_list_organizations(client):
    organizations = client.organizations.list()
    assert organizations.results, "Expected a non-empty list of organizations."


def test_retrieve_organization(client):
    organizations = client.organizations.list()
    org_id = organizations.results[0].id
    organization = client.organizations.retrieve(org_id)
    assert organization.id == org_id


def test_list_requests(client):
    requests = client.requests.list()
    assert requests, "Expected a non-empty list of requests."


def test_retrieve_request(client):
    request = client.requests.retrieve(17)
    assert request.id == 17


def test_list_users(client):
    users = client.users.list()
    assert users.results, "Expected a non-empty list of users."


def test_retrieve_user(client):
    users = client.users.list()
    user_id = users.results[0].id
    user = client.users.retrieve(user_id)
    assert user.id == user_id


def test_list_projects(client):
    projects = client.projects.list()
    assert projects, "Expected a non-empty list of projects."


def test_retrieve_project(client):
    project = client.projects.retrieve(10)
    assert project.id == 10

def test_create_request(client):
    new_request = client.requests.create(
        title="Test FOIA Request",
        requested_docs="This is a test FOIA request.",
        organization=1,
        agencies=[248],
    )
    assert "test-foia-request" in new_request

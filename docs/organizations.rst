Organization
===========

Methods for searching and retrieving organizations. 

OrganizationClient
----------------
.. class:: documentcloud.organizations.OrganizationClient

  The organization client allows access to search, list, and retrieve individual organizations.
  Accessed generally as ``client.organizations``. 

  .. method:: list(self, **params)

    List all organizations with optional filtering. Available filters include:

    - **name**: Filter by the organization name.
    - **slug**: Filter by the organization's slug (URL identifier).
    - **uuid**: Filter by the unique identifier for the organization.

    :param params: Query parameters to filter results, such as `name`, `slug`, and `uuid`
    :return: An :class:`APIResults` object containing the list of organizations.

  .. method:: retrieve(self, organization_id)

    Retrieve a specific organization by its ID.

    :param organization_id: The unique ID of the organization to retrieve.
    :return: An :class:`Organization` object representing the requested organization.


Organization
----------------
.. class:: documentcloud.organizations.Organization

  A representation of a single organization.

  .. method:: str()

    Return a string representation of the organization in the format `Organization {id} - Name: {name}`.

  .. attribute:: id

    The numerical unique ID of the organization.

  .. attribute:: name

    The name of the organization.

  .. attribute:: slug

    The URL-friendly identifier (slug) for the organization.

  .. attribute:: uuid

    The unique identifier for the organization (UUID format).

  .. attribute:: individual

    A boolean indicating if the organization is an individual organization or not.

  .. attribute:: entitlement

    The ID of the entitlements associated with the organization.

  .. attribute:: verified_journalist

    A boolean indicating if the organization is verified as a journalist. This allows members of this organization to upload documents to DocumentCloud among other things. 

  .. attribute:: users

    A list of user IDs associated with the organization.
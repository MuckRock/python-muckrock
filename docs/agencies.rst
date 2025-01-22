Agencies
===========

Methods for searching and retrieving agencies. 

AgencyClient
----------------

.. class:: muckrock.agencies.AgencyClient
   The agency client allows access to search and retrieval of agencies via the MuckRock API. The client supports querying, listing, and retrieving specific agencies.

  .. method:: list(self, **params)
    List all agencies with optional filtering by parameters. Filters include:
      - **name**: The agency name. Partial matches are supported.
      - **jurisdiction**: the ID of the Jurisidiction the agency belongs to. 
    :param params: Query parameters to filter results (e.g., `jurisdiction`, `name`).
    :return: An :class:`APIResults` object containing the list of agencies.

  .. method:: retrieve(self, agency_id)
    Retrieve a specific agency by its unique identifier.
    :param agency_id: The unique ID of the agency to retrieve.
    :return: An :class:`Agency` object representing the requested agency.


Agency
----------------
.. class:: muckrock.agencies.Agency

  A representation of a single agency.

  .. method:: str()
    Returns a string representation of the agency, which is the `name` of the agency.

  .. attribute:: id
    The unique identifier for the agency.

  .. attribute:: name
    The name of the agency.

  .. attribute:: slug
    The slug (URL identifier) for the agency.

  .. attribute:: status
    The current operational status of the agency (e.g., pending, approved, rejected).

  .. attribute:: exempt
    Indicates whether the agency is exempt from records laws

  .. attribute:: types
    A list of types of agency (e.g., Police, Transportation, Military).

  .. attribute:: requires_proxy
    Indicates whether the agency requires a proxy because of in-state residency laws.

  .. attribute:: jurisdiction
    The jurisdiction to which the agency belongs.

  .. attribute:: parent
    The ID of the parent agency

  .. attribute:: appeal_agency
    The ID of the agency to which appeals are directed

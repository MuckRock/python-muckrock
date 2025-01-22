Jurisdictions
===========

Methods for searching and retrieving jurisdictions. 

JurisdictionClient
----------------
.. class:: documentcloud.jurisdictions.JurisdictionClient

  The jurisdiction client allows access to search, list, and retrieve individual jurisdictions.

  .. method:: list(self, **params)

    List all jurisdictions with optional filtering. Available filters include:

    - **abbrev**: Filter by the jurisdiction abbreviation. Local jurisdictions typically don't have an abbreviation.
    - **level**: Filter by the level of the jurisdiction (e.g., `f` for Federal, `s` for State, `l` for Local).
    - **name**: Filter by the jurisdiction's name.
    - **parent**: Filter by the ID of the parent jurisdiction. Jurisdictions can have a federal or state parent, while local jurisdictions cannot be parents.

    :param params: Query parameters to filter results, such as `abbrev`, `level`, `name`, and `parent`.
    :return: An :class:`APIResults` object containing the list of jurisdictions.

  .. method:: retrieve(self, jurisdiction_id)

    Retrieve a specific jurisdiction by its unique identifier.

    :param jurisdiction_id: The unique ID of the jurisdiction to retrieve.
    :return: A :class:`Jurisdiction` object representing the requested jurisdiction.

Jurisdiction
----------------
.. class:: documentcloud.jurisdictions.Jurisdiction

  A representation of a jurisdiction. 

  .. method:: str()

    Return a string representation of the jurisdiction - its `name`.

  .. attribute:: id

    The unique identifier for the jurisdiction.

  .. attribute:: name

    The name of the jurisdiction.

  .. attribute:: slug

    The URL-friendly identifier for the jurisdiction.

  .. attribute:: abbrev

    The abbreviation for the jurisdiction. Local jurisdictions do not have one.

  .. attribute:: level

    The level of the jurisdiction, which can be:
    - **`f`** for Federal
    - **`s`** for State
    - **`l`** for Local

  .. attribute:: parent

    The ID of the parent jurisdiction, defining the hierarchy between jurisdictions. A jurisdiction can have a federal or state parent, while local jurisdictions cannot be parents.

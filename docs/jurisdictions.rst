Jurisdictions
===========

Methods for searching and retrieving jurisdictions. 

JurisdictionClient
----------------
.. class:: documentcloud.jurisdictions.JurisdictionClient

  The jurisdiction client allows access to search, list, and retrieve individual jurisdictions. Accessed generally as ``client.jurisdictions``. 
  ::

    >>> jurisdiction_list = client.jurisdictions.list(level='s')
    >>> jurisdiction_list
      <APIResults: [<Jurisdiction: 1 - Massachusetts>, <Jurisdiction: 13 - Maine>, <Jurisdiction: 16 - New York>, <Jurisdiction: 34 - Florida>, <Jurisdiction: 47 - District of Columbia>, <Jurisdiction: 52 - California>, <Jurisdiction: 53 - Connecticut>, <Jurisdiction: 54 - Washington>, <Jurisdiction: 78 - Arizona>, <Jurisdiction: 80 - Vermont>, <Jurisdiction: 81 - New Hampshire>, <Jurisdiction: 82 - Rhode Island>, <Jurisdiction: 109 - Texas>, <Jurisdiction: 111 - Kansas>, <Jurisdiction: 114 - Arkansas>, <Jurisdiction: 116 - Ohio>, <Jurisdiction: 117 - Michigan>, <Jurisdiction: 126 - Pennsylvania>, <Jurisdiction: 127 - Colorado>, <Jurisdiction: 128 - Virginia>, <Jurisdiction: 146 - Wisconsin>, <Jurisdiction: 147 - Kentucky>, <Jurisdiction: 152 - Indiana>, <Jurisdiction: 153 - North Carolina>, <Jurisdiction: 154 - Maryland>, <Jurisdiction: 155 - Tennessee>, <Jurisdiction: 156 - Minnesota>, <Jurisdiction: 157 - Montana>, <Jurisdiction: 158 - Oregon>, <Jurisdiction: 159 - Alabama>, <Jurisdiction: 168 - Illinois>, <Jurisdiction: 227 - New Mexico>, <Jurisdiction: 228 - Idaho>, <Jurisdiction: 229 - New Jersey>, <Jurisdiction: 230 - Georgia>, <Jurisdiction: 231 - Mississippi>, <Jurisdiction: 232 - North Dakota>, <Jurisdiction: 233 - Louisiana>, <Jurisdiction: 234 - Utah>, <Jurisdiction: 235 - Alaska>, <Jurisdiction: 236 - Delaware>, <Jurisdiction: 246 - Iowa>, <Jurisdiction: 247 - Hawaii>, <Jurisdiction: 248 - Oklahoma>, <Jurisdiction: 299 - Missouri>, <Jurisdiction: 300 - Nebraska>, <Jurisdiction: 301 - Nevada>, <Jurisdiction: 302 - South Carolina>, <Jurisdiction: 303 - South Dakota>, <Jurisdiction: 304 - West Virginia>]>

    >>> kentucky = client.jurisdictions.retrieve(147)
    >>> kentucky.abbrev 
      'KY'

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

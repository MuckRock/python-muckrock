Agencies
===========

Methods for searching and retrieving agencies. 

AgencyClient
----------------

.. class:: muckrock.agencies.AgencyClient

   The agency client allows access to search and retrieval of agencies via the MuckRock API. The client supports querying, listing, and retrieving specific agencies. Accessed generally as ``client.agencies``.
   ::
    >>> example_agency = client.agencies.retrieve(453)
    >>> example_agency
    <Agency: 453 - Executive Office of Public Safety and Security>

    >>> agency_search_example = client.agencies.list(jurisdiction__id=1)
    >>> agency_search_example
      <APIResults: [<Agency: 18 - Department of Transitional Assistance>, <Agency: 26 - Office of Consumer Affairs and Business Regulation>, <Agency: 31 - Department of Education>, <Agency: 73 - Massachusetts State Lottery>, <Agency: 118 - Massachusetts Bay Transportation Authority (MBTA)>, <Agency: 123 - State Racing Commission>, <Agency: 131 - Parole Board>, <Agency: 138 - Executive Office of Health and Human Services>, <Agency: 139 - Human Resources Division>, <Agency: 141 - Office of the Comptroller>, <Agency: 146 - Executive Office for Administration and Finance>, <Agency: 154 - Commonwealth Health Insurance Connector Authority>, <Agency: 155 - Division of Insurance>, <Agency: 156 - Office of Medicaid>, <Agency: 159 - Office of Medicaid>, <Agency: 160 - Massachusetts Technology Collaborative>, <Agency: 161 - Executive Office of Housing and Economic Development>, <Agency: 162 - Department of Transportation>, <Agency: 163 - MassDevelopment>, <Agency: 164 - MassDevelopment>, <Agency: 171 - Massachusetts Clean Energy Center>, <Agency: 175 - Department of Revenue>, <Agency: 191 - Elections Division (Secretary of State)>, <Agency: 192 - University of Massachusetts>, <Agency: 193 - University of Massachusetts (Amherst)>, <Agency: 195 - Massachusetts Emergency Management Agency>, <Agency: 196 - University of Massachusetts School of Law>, <Agency: 230 - The Massachusetts Historical Commission>, <Agency: 231 - Department of Youth Services>, <Agency: 257 - Massachusetts Department of Criminal Justice Information Services>, <Agency: 267 - Division of Health Care Finance and Policy>, <Agency: 274 - Massachusetts State Police>, <Agency: 310 - Department of Correction>, <Agency: 330 - Supervisor of Public Records>, <Agency: 331 - Department of Public Safety, Architectural Access Board>, <Agency: 332 - Office of Consumer Affairs and Business Regulation Massachusetts, Consumer Assistance Unit>, <Agency: 410 - Registry of Motor Vehicles>, <Agency: 411 - Massachusetts Commission on Lesbian, Gay, Bisexual, Transgender, Queer and Questioning (LGBTQ) Youth (Commission)>, <Agency: 412 - Department of Children and Families>, <Agency: 432 - Department of Public Safety>, <Agency: 433 - Office of the Governor - Massachusetts>, <Agency: 443 - Inspector General>, <Agency: 452 - Commonwealth Fusion Center>, <Agency: 453 - Executive Office of Public Safety and Security>, <Agency: 480 - Massachusetts Port Authority>, <Agency: 501 - Energy Facilities Siting Board>, <Agency: 508 - Attorney General's Office>, <Agency: 562 - Department of Public Utilities>, <Agency: 651 - Metropolitan Law Enforcement Council (MetroLEC)>, <Agency: 714 - Department of Public Health, Division of Health Care Quality>]>

  .. method:: list(self, **params)

     List all agencies with optional filtering by parameters. Filters include:
      - name: The agency name. Partial matches are supported.
      - jurisdiction__id: the ID of the Jurisidiction the agency belongs to. 
    :param params: Query parameters to filter results (e.g., `jurisdiction`, `name`).
    :return: An :class:`APIResults` object containing the list of agencies.

  .. method:: retrieve(self, agency_id)

    Retrieve a specific agency by its unique identifier.

    :param agency_id: The unique ID of the agency to retrieve.
    :return: A :class:`Agency` object representing the requested agency.


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

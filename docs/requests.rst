Requests
===========

Methods for searching, retrieving, and creating FOIA requests. 

RequestClient
----------------
.. class:: muckrock.requests.RequestClient

  The request client allows access to search, list, create, and retrieve FOIA requests. Accessed generally as ``client.requests``. 
  Refer to the getting started page to look at some examples of searching and filing requests. 

  To find requests within a date range, use the ``__gte`` (on or after) and ``__lte`` (on or before) filters with dates in ``YYYY-MM-DD`` format. They can be combined with other filters such as ``agency``:
  ::

    >>> requests_2024 = client.requests.list(datetime_submitted__gte='2024-01-01', datetime_submitted__lte='2024-12-31')
    >>> agency_requests_2024 = client.requests.list(agency=453, datetime_submitted__gte='2024-01-01', datetime_submitted__lte='2024-12-31')

  .. method:: list(self, **params)

    List all FOIA requests with optional filtering. Available filters include:

    - **user**: Filter by the user ID of the person who filed the request.
    - **title**: Filter by the title of the request.
    - **status**: Filter by the status of the request (e.g., "submitted", "ack", "processed").
    - **embargo_status**: Filter by the embargo status (e.g., "public", "embargo", "permanent").
    - **agency**: Filter by the agency ID handling the request.
    - **tags**: Filter by tags associated with the request.
    - **jurisdiction**: Filter by the jurisdiction ID associated with the request.
    - **datetime_submitted__gte**: Requests submitted on or after this date.
    - **datetime_submitted__lte**: Requests submitted on or before this date.
    - **datetime_updated__gte**: Requests last updated on or after this date.
    - **datetime_updated__lte**: Requests last updated on or before this date.
    - **datetime_done__gte**: Requests where the response was received on or after this date.
    - **datetime_done__lte**: Requests where the response was received on or before this date.
    - **search**: An optional search term. For example, you can search for any request that mentions recipes. 

    :param params: Query parameters to filter results, such as `user`, `title`, `status`, `embargo_status`, `agency`, `tags`, `jurisdiction`, the date range filters, and `search`.
    :return: An :class:`APIResults` object containing the list of FOIA requests.

  .. method:: retrieve(self, request_id)

    Retrieve a specific FOIA request by its unique numerical identifier (ID).

    :param request_id: The unique ID of the FOIA request to retrieve.
    :return: A :class:`Request` object representing the requested FOIA request.

  .. method:: create(self, title, requested_docs, organization, agencies, embargo_status="public", **kwargs)

    Create a new FOIA request.

    :param title: The title of the FOIA request. (Required)
    :param requested_docs: A description of the documents being requested. (Required)
    :param organization: The ID of the organization requesting the FOIA documents. (Required)
    :param agencies: A list of agency IDs involved in the request. (Required)
    :param embargo_status: The embargo status of the request (default is "public"). Embargoing requires a paid subscription. 
    :param edited_boilerplate: If ``True``, ``requested_docs`` is used as the full text of the request instead of being inserted into MuckRock's standard request template (default is ``False``). Passed through ``kwargs``. Note that this also skips the proxy template language included for agencies in states with in-state residency requirements.
    :param kwargs: Additional parameters to be included in the request.
    :return: A URL linking to the newly created FOIA request(s).
    :raises: ValueError if `agencies` is not a non-empty list.


Request
----------------
.. class:: muckrock.requests.Request

  A representation of a single FOIA request.

  .. method:: str()

    Return a string representation of the FOIA request, which is the request title.

  .. method:: get_communications(self)

    Retrieve all communications associated with this FOIA request.

    This method fetches all communications related to the specific FOIA request. If no communications are found, it returns an empty :class:`APIResults` object.

    :return: An :class:`APIResults` object containing the list of communications.

  .. attribute:: id

    The unique identifier for this FOIA request.

  .. attribute:: title

    The title of the FOIA request.

  .. attribute:: requested_docs

    A description of the documents being requested.

  .. attribute:: slug

    The slug (URL identifier) for the FOIA request.

  .. attribute:: status

    The current status of the FOIA request, represented as one of these values:

    - "submitted" - Processing
    - "ack" - Awaiting Acknowledgement
    - "processed" - Awaiting Response
    - "appealing" - Awaiting Appeal
    - "fix" - Fix Required
    - "payment" - Payment Required
    - "lawsuit" - In Litigation
    - "rejected" - Rejected
    - "no_docs" - No Responsive Documents
    - "done" - Completed
    - "partial" - Partially Completed
    - "abandoned" - Withdrawn

  .. attribute:: agency

    The ID of the agency that the request was submitted to.

  .. attribute:: composer

    The ID of the composer that created this request. Requests filed together in a multi-request share the same composer.

  .. attribute:: embargo_status

    The embargo status of the request, indicating its visibility. Options include:
  
    - "public" - Public
    - "embargo" - Embargo (only available to paid professional users)
    - "permanent" - Permanent Embargo (only available to paid organizational members)

  .. attribute:: user

    The user ID of the person who filed this request.

  .. attribute:: edit_collaborators

    A list of user IDs who have been given edit access to this request.

  .. attribute:: read_collaborators

    A list of user IDs who have been given view access to this request.

  .. attribute:: datetime_submitted

    The timestamp of when this request was submitted.

  .. attribute:: datetime_updated

    The date and time when the request was last updated.

  .. attribute:: datetime_done

    The date and time when the request was completed, if applicable.

  .. attribute:: tracking_id

    The tracking ID assigned to this request by the agency.

  .. attribute:: price

    The cost of processing this request, if applicable.

  .. attribute:: tags

    A list of tags associated with this request.

  .. attribute:: edited_boilerplate

    A boolean indicating whether ``requested_docs`` was used as the full text of the request instead of MuckRock's standard request template.

  .. attribute:: date_due

    The date a response from the agency is due, based on the statutory deadline for the request's jurisdiction.
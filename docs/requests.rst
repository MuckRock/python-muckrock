Requests
===========

Methods for searching, retrieving, and creating FOIA requests. 

RequestClient
----------------
.. class:: documentcloud.requests.RequestClient
  The request client allows access to search, list, create, and retrieve FOIA requests.

  .. method:: list(self, **params)
    List all FOIA requests with optional filtering and ordering. Available filters include:

    - **user**: Filter by the user ID of the person who filed the request.
    - **title**: Filter by the title of the request.
    - **status**: Filter by the status of the request (e.g., "submitted", "ack", "processed").
    - **embargo_status**: Filter by the embargo status (e.g., "public", "embargo", "permanent").
    - **agency**: Filter by the agency ID handling the request.
    - **tags**: Filter by tags associated with the request.
    - **jurisdiction**: Filter by the jurisdiction ID associated with the request.

    Ordering options are available, including:

    - **title**: Sort by the request title.
    - **status**: Sort by the request status.
    - **agency**: Sort by the agency handling the request.
    - **user**: Sort by the user who filed the request.
    - **datetime_submitted**: Sort by the date the request was submitted.
    - **datetime_done**: Sort by the date the request was completed.

    Ordering can be specified as either ascending (`ordering=user`) or descending (`ordering=-user`).

    :param params: Query parameters to filter and order results, such as `user`, `title`, `status`, `embargo_status`, `agency`, `tags`, and `jurisdiction`, along with `ordering`.
    :return: An :class:`APIResults` object containing the list of FOIA requests.

  .. method:: retrieve(self, request_id)
    Retrieve a specific FOIA request by its unique numerical identifier (ID).

    :param request_id: The unique ID of the FOIA request to retrieve.
    :return: A :class:`Request` object representing the requested FOIA request.

  .. method:: create(self, title, requested_docs, organization, agencies, embargo_status="public", **kwargs)
    Create a new FOIA request.

    :param title: The title of the FOIA request. (Required)
    :param requested_docs: A description of the documents being requested. (Required)
    :param organization: The ID of the organization requesting the FOIA documents.
    :param agencies: A list of agency IDs involved in the request. (Required)
    :param embargo_status: The embargo status of the request (default is "public").
    :param kwargs: Additional parameters to be included in the request.
    :return: A URL linking to the newly created FOIA request(s).
    :raises: ValueError if `agencies` is not a non-empty list.


Request
----------------
.. class:: documentcloud.requests.Request
  A representation of a single FOIA request.

  .. method:: str()
    Return a string representation of the FOIA request, which is the request title.

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

Files
===========

Methods for searching and retrieving files attached to FOIA communications. 

FileClient
----------------
.. class:: documentcloud.files.FileClient

  The file client allows access to search, list, and retrieve individual FOIA files. 

  .. method:: list(self, **params)
    List all FOIA files with optional filtering. Available filters include:

    - **communication**: Filter by the associated communication's ID.
    - **title**: Filter by the file title.
    - **doc_id**: Filter by unique identifier for the document (different than the ID of the file).

    :param params: Query parameters to filter results, such as `communication`, `title`, and `doc_id`.
    :return: An :class:`APIResults` object containing the list of files.

  .. method:: retrieve(self, file_id)

    Retrieve a specific FOIA file by its unique identifier.

    :param file_id: The unique ID of the file to retrieve.
    :return: A :class:`File` object representing the requested file.

File
----------------
.. class:: documentcloud.files.File

  A representation of a single FOIA file.

  .. method:: str()
    Returns a string representation of the file in the format: `File {id} - Title: {title}`.

  .. attribute:: id
    The unique identifier for the file.

  .. attribute:: ffile
    The URL of the file.

  .. attribute:: datetime
    The date and time when the file was uploaded.

  .. attribute:: title
    The title of the file.

  .. attribute:: source
    The source of the file (e.g., the agency or department).

  .. attribute:: description
    A description of the file.

  .. attribute:: doc_id
    Filter by the document identifier assigned to the file.

  .. attribute:: pages
    The number of pages in the file.

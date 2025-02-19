Projects
===========

Methods for searching and retrieving projects. 

ProjectClient
----------------
.. class:: documentcloud.projects.ProjectClient

The project client allows access to search, list, and retrieve projects.  Accessed generally as ``client.projects``. 
  ::

.. method:: list(self, **params)

    List all projects with optional filtering. Available filters include:

    - **contributors**: Filter by the unique identifier of a user associated with the project.
    - **requests**: Filter by projects which have this request associated with it.
    - **title**: Filter by the title of the project. Supports partial matches. Case sensitive.

    :param params: Query parameters to filter results, such as `contributors`, `requests`, and `title`.
    :return: An :class:`APIResults` object containing the list of projects.

.. method:: retrieve(self, project_id)

    Retrieve a specific project by its ID

    :param project_id: The unique ID of the project to retrieve.
    :return: A :class:`Project` object representing the requested project.

Project
----------------
.. class:: documentcloud.projects.Project

  A representation of a single project.

  .. method:: str()

    Return a string representation of the project in format: `Project {id} - Title: {title}`.

  .. attribute:: id

    The unique numerical identifier for the project.

  .. attribute:: title

    The title of the project.

  .. attribute:: slug

    A short, URL-friendly version of the project's title.

  .. attribute:: summary

    A brief summary of the project.

  .. attribute:: description

    A detailed description of the project.

  .. attribute:: image

    The image associated with the project (if available).

  .. attribute:: private

    A boolean indicating whether the project is private (`true`) or public (`false`).

  .. attribute:: approved

    A boolean indicating whether the project has been approved (`true`) or not (`false`).

  .. attribute:: featured

    A boolean indicating whether the project is featured on the MuckRock site (`true`) or not (`false`).

  .. attribute:: contributors

    A list of user IDs representing the contributors to the project.

  .. attribute:: articles

    A list of article IDs associated with the project.

  .. attribute:: requests

    A list of request IDs associated with the project.

  .. attribute:: date_created

    The date and time when the project was created. If null, the creation date is not set.

  .. attribute:: date_approved

    The date and time when the project was approved. If null, the approval date is not set.
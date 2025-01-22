Users
===========

Methods for searching and retrieving users. 

UserClient
----------------
.. class:: documentcloud.users.UserClient

  The user client allows access to search, list, and retrieve individual users.  Accessed generally as ``client.organizations``. 
  ::
    >>> my_user = client.users.me()

  .. method:: me(self)

    Retrieve the currently authenticated user.

    :return: A :class:`User` object representing the authenticated user.

  .. method:: list(self, **params)

    List all users with optional filtering. Available filters include:

    - **id**: Filter by the unique identifier of the user.
    - **full_name**: Filter by the full name of the user.
    - **username**: Filter by the username of the user.
    - **uuid**: Filter by the unique identifier for the user's profile.
    - **email**: Filter by the user's email address.

    :param params: Query parameters to filter results, such as `id`, `full_name`, `username`, `uuid`, and `email`.
    :return: An :class:`APIResults` object containing the list of users.

  .. method:: retrieve(self, user_id)

    Retrieve a specific user by their ID

    :param user_id: The unique ID of the user to retrieve.
    :return: A :class:`User` object representing the requested user.


User
----------------
.. class:: documentcloud.users.User

  A representation of a single user.

  .. method:: str()

    Return a string representation of the user in format: `User {id} - Username: {username}, Email: {email}`.

  .. attribute:: id

    The unique numerical identifier for the user.

  .. attribute:: username

    The unique username of the user.

  .. attribute:: email

    The email address of the user.

  .. attribute:: last_login

    The date and time when the user last logged in.

  .. attribute:: date_joined

    The date and time when the user joined.

  .. attribute:: full_name

    The full name of the user.

  .. attribute:: uuid

    The unique identifier for the user's profile (UUID format).

  .. attribute:: organizations

    A list of organization IDs the user belongs to.

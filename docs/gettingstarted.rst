Getting started
===============

This tutorial will walk you through the process of installing python-muckrock and making your first requests.

Installation
------------

Provided that you have `pip <http://pypi.python.org/pypi/pip>`_ installed, you can install the library like so: ::

    $ pip install python-muckrock

Creating a client
-----------------

Before you can interact with MuckRock, you first must import the library and initialize a client to talk with the site on your behalf. ::

    >>> from muckrock import MuckRock
    >>> client = MuckRock(USERNAME, PASSWORD)

You can also specify a custom uri if you have installed your own version of MuckRock ::

    >>> client = MuckRock(USERNAME, PASSWORD, base_uri="https://your.documentcloud.domain/api/", auth_uri="https://your.account.server.domain/api/")

If you need to debug, you can pass a logging level as a parameter to the client when you instantiate. You will need to import logging first. There are several `logging levels <https://docs.python.org/3/library/logging.html#logging-levels>`_ depending on your needs. For this example, we will use the DEBUG level. ::

    >>> import logging
    >>> client = MuckRock(USERNAME, PASSWORD, loglevel=logging.DEBUG)

Searching for requests
-----------------------

You can now you use the client to interact with the MuckRock API. A search for requests about recipes would look like this: ::

    >>> request_list = client.requests.list(search="Recipe")
    >>> request_list
    <APIResults: [<Request: 62755 - 2014 Black Bear Recipe Guide development documents>, <Request: 48151 - CIA recipes and cookbooks>, <Request: 33761 - CIA's Pseudo-Marijuana Recipe>, <Request: 109529 - Food recipe request (San Francisco Fire Department)>, <Request: 21691 - UConn’s Bacon Jalapeño Macaroni and Cheese Recipe>]>

The response will be a set of requests with each request labelled with its ID (62755 for example), then the request title. The results are paginated, so if there are more than 25 results returned, you can use `.next` and `.previous` to traverse the results. You may view the next 25 results like so 

::
    >>> request_list.next 


Retrieving a single request
-----------------------

Let's say we want to retrieve a single request (like request 62755 from above).. 
You may retrieve this single request by its ID like so: ::

    >>> request_test = client.requests.retrieve(62755)
    >>> request_test
    <Request: 48151 - CIA recipes and cookbooks>


Retrieving your organization ID
-----------------------

To file requests using the API, you need to know which organization to file the requests under. 
The easiest way to find the organization IDs of organizations you belong to is by accessing the user endpoint. ::

    >>> my_user = client.users.me()
    >>> my_user
    <User: 15499 - User 15499 - Username: sanjin, Email: sanjin@muckrock.com>
    >>> my_user.organizations
    [1, 24695]

You may decide which organization to file under depending on which one has available credits remaining. You may retrieve an organization by its ID to help you decide which one to file under like so: ::

    >>> my_first_org = client.organizations.retrieve(1)
    >>> my_first_org
    <Organization: 1 - Organization 1 - Name: MuckRock Staff>


Searching for agencies
-----------------------
Before you can file a request using the MuckRock API, you need to know where to file the request. 
Similar to the requests endpoint, the agencies endpoint has filters that allow you to find the agencies of interest. 
You can provide a search term or other filter. Consult the agencies portion of this documentation for more options. 

Here is an example of how to find agencies that belong to jurisdiction 1 (Massachusetts)

::

    >>> agency_list = client.agencies.list(jurisdiction__id=1)
    >>> agency_list
    <APIResults: [<Agency: 18 - Department of Transitional Assistance>, <Agency: 26 - Office of Consumer Affairs and Business Regulation>, <Agency: 31 - Department of Education>, <Agency: 73 - Massachusetts State Lottery>, <Agency: 118 - Massachusetts Bay Transportation Authority (MBTA)>, <Agency: 123 - State Racing Commission>, <Agency: 131 - Parole Board>, <Agency: 138 - Executive Office of Health and Human Services>, <Agency: 139 - Human Resources Division>, <Agency: 141 - Office of the Comptroller>, <Agency: 146 - Executive Office for Administration and Finance>, <Agency: 154 - Commonwealth Health Insurance Connector Authority>, <Agency: 155 - Division of Insurance>, <Agency: 156 - Office of Medicaid>, <Agency: 159 - Office of Medicaid>, <Agency: 160 - Massachusetts Technology Collaborative>, <Agency: 161 - Executive Office of Housing and Economic Development>, <Agency: 162 - Department of Transportation>, <Agency: 163 - MassDevelopment>, <Agency: 164 - MassDevelopment>, <Agency: 171 - Massachusetts Clean Energy Center>, <Agency: 175 - Department of Revenue>, <Agency: 191 - Elections Division (Secretary of State)>, <Agency: 192 - University of Massachusetts>, <Agency: 193 - University of Massachusetts (Amherst)>, <Agency: 195 - Massachusetts Emergency Management Agency>, <Agency: 196 - University of Massachusetts School of Law>, <Agency: 230 - The Massachusetts Historical Commission>, <Agency: 231 - Department of Youth Services>, <Agency: 257 - Massachusetts Department of Criminal Justice Information Services>, <Agency: 267 - Division of Health Care Finance and Policy>, <Agency: 274 - Massachusetts State Police>, <Agency: 310 - Department of Correction>, <Agency: 330 - Supervisor of Public Records>, <Agency: 331 - Department of Public Safety, Architectural Access Board>, <Agency: 332 - Office of Consumer Affairs and Business Regulation Massachusetts, Consumer Assistance Unit>, <Agency: 410 - Registry of Motor Vehicles>, <Agency: 411 - Massachusetts Commission on Lesbian, Gay, Bisexual, Transgender, Queer and Questioning (LGBTQ) Youth (Commission)>, <Agency: 412 - Department of Children and Families>, <Agency: 432 - Department of Public Safety>, <Agency: 433 - Office of the Governor - Massachusetts>, <Agency: 443 - Inspector General>, <Agency: 452 - Commonwealth Fusion Center>, <Agency: 453 - Executive Office of Public Safety and Security>, <Agency: 480 - Massachusetts Port Authority>, <Agency: 501 - Energy Facilities Siting Board>, <Agency: 508 - Attorney General's Office>, <Agency: 562 - Department of Public Utilities>, <Agency: 651 - Metropolitan Law Enforcement Council (MetroLEC)>, <Agency: 714 - Department of Public Health, Division of Health Care Quality>]>


Filing a single request
-----------------------

Filing a single request is similar to filing a multi-request, except that single requests do not go through a review process. Calling create returns the link to your request(s). You may file a single request like so: ::
    
    >>> new_request_data = {
        "title": "Your request title here",
        "requested_docs": "This is a test FOIA request.",
        "organization": 1, # You must replace this with the integer of an organization you have access to. 
        "agencies": [248],  # Replace this with the ID of the actual agency you plan on filing with. 
    }
    >>> new_request = client.requests.create(**new_request_data)
    https://www.muckrock.com/foi/multirequest/your-request-title-here-151010/


Filing a multi-request
-----------------------
The only difference between filing a single and multi-request is that you provide multiple agencies.
:: 

    >>> new_request_data = {
        "title": "Your request title here",
        "requested_docs": "This is a test FOIA request.",
        "organization": 1 # Replace this with your org id, 
        "agencies": [248, 18529]  # Replace this with your list of agencies. 
    }
    >>> new_request = client.requests.create(**new_request_data)
    https://www.muckrock.com/foi/multirequest/your-request-title-here-151010/

You may still edit or delete the request before it is filed (30 minutes after creation) on the site.

Finding communications and files tied to a request
-----------------------

We can find communications and files (to download them for example) tied to a request in two steps once we have the request ID. First, we query communications by the request ID to grab the communications for the request in question. If there are more than 25 communications on a request you will have to use .next to grab the next page of communications.

:: 

    >>> >>> comms_list = client.communications.list(foia=14313)
    >>> comms_list
    <APIResults: [<Communication: 108835 - Communication 108835>, <Communication: 108843 - Communication 108843>, <Communication: 108907 - Communication 108907>, <Communication: 108966 - Communication 108966>, <Communication: 111795 - Communication 111795>, <Communication: 116217 - Communication 116217>, <Communication: 117300 - Communication 117300>, <Communication: 125824 - Communication 125824>, <Communication: 126598 - Communication 126598>, <Communication: 132173 - Communication 132173>, <Communication: 132516 - Communication 132516>, <Communication: 137925 - Communication 137925>, <Communication: 138088 - Communication 138088>, <Communication: 145537 - Communication 145537>, <Communication: 152476 - Communication 152476>, <Communication: 152664 - Communication 152664>, <Communication: 160437 - Communication 160437>, <Communication: 160672 - Communication 160672>, <Communication: 168785 - Communication 168785>, <Communication: 169623 - Communication 169623>, <Communication: 178866 - Communication 178866>, <Communication: 179077 - Communication 179077>, <Communication: 191560 - Communication 191560>, <Communication: 201224 - Communication 201224>, <Communication: 209319 - Communication 209319>, <Communication: 210054 - Communication 210054>, <Communication: 217196 - Communication 217196>, <Communication: 217378 - Communication 217378>, <Communication: 224981 - Communication 224981>, <Communication: 225368 - Communication 225368>, <Communication: 232374 - Communication 232374>, <Communication: 232639 - Communication 232639>, <Communication: 240709 - Communication 240709>, <Communication: 240818 - Communication 240818>, <Communication: 249100 - Communication 249100>, <Communication: 250002 - Communication 250002>, <Communication: 257558 - Communication 257558>, <Communication: 258751 - Communication 258751>, <Communication: 266697 - Communication 266697>, <Communication: 267332 - Communication 267332>, <Communication: 277200 - Communication 277200>, <Communication: 277719 - Communication 277719>, <Communication: 285848 - Communication 285848>, <Communication: 285988 - Communication 285988>, <Communication: 294296 - Communication 294296>, <Communication: 294402 - Communication 294402>, <Communication: 304474 - Communication 304474>, <Communication: 304853 - Communication 304853>, <Communication: 314973 - Communication 314973>, <Communication: 315197 - Communication 315197>]>
   


We can then loop through each communication to see which ones have attached files. We can append the file IDs to a list for easier access later. :: 

    >>> file_ids = []
    >>> for communication in comms_list:
            # Check if the communication has files
            if communication.files:
                # Append the file IDs to the file_ids list
                file_ids.extend(communication.files)

    >>> print(file_ids)
    >>> [30713, 30784, 31777, 32802, 32803, 35050, 35051, 36933, 36934, 38807, 38808, 45602, 48352, 51338, 54365, 66321, 71173, 74419, 77104, 84246, 87396, 94028, 96561, 100048, 103091, 105814, 109429, 113222, 116546, 121632, 127366, 131921, 136311, 140504, 152006, 155724, 911255, 912763, 917387, 917386, 917385, 917384, 920439, 1150693, 1150694]


Now that we have the file IDs for the request we can access the link to each file using the files endpoint. :: 


    >>> for file_id in file_ids:
            file_obj = client.files.retrieve(file_id)
            print(file_obj.ffile)
    >>>       
    https://cdn.muckrock.com/foia_files/WRD000_244.jpg
    https://cdn.muckrock.com/foia_files/WRD345.jpg
    https://cdn.muckrock.com/foia_files/12-2-14_MR14313_INT_ID1313992-000.pdf
    ... 
    https://cdn.muckrock.com/foia_files/2024/02/01/20-00038-FR.pdf
    https://cdn.muckrock.com/foia_files/2024/02/01/REFERRAL_DETERMINATION.docx

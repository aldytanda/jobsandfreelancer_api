## How to run the API

In the project directory, you can run:

	$ python manage.py run 
or 

	$ python3 manage.py run 

depending on which version of python is installed in the machine.
I guess there should also be a virtualenv or virtualenvwrapper installed. I used this command to install the virtual env

	$ sudo pip3 install virtualenvwrapper

If the app is successfuly run, you will see below messages in your terminal

 * Debug mode: on
 * Running on http://127.0.0.1:5000/ 
 * Debugger is active!
 * Debugger PIN: 123-456-789


## Using the API

Flask-restplus provided me with Swagger automatic documentation, which can be accessed through localhost:

### `http://localhost:5000/`

here's the full list of avaialble end points:
* GET /job/

	List all registered jobs


* GET /job/page/{page}?title={title}  

	List registered jobs with server-side pagination and filter by Job Title

* POST /job/

	Creates a new Job

* GET /job/{id}

	Get a job given its identifier (id)

* DELETE /job/{id} 

	Delete a job given its identifier

* PUT /job/{id}

	Update a Job

* POST /job/{id}

	Assign freelancer to the job (provide freelancer_id in request body)

* GET /freelancer/

	List all registered freelancers

* GET /freelancer/page/{page}?title={title}  

	List registered freelancers with server-side pagination and filter by freelancer Title

* POST /freelancer/

	Creates a new freelancer

* GET /freelancer/{id}

	Get a freelancer given its identifier (id)


* DELETE /freelancer/{id} 

	Delete a freelancer given its identifier

* PUT /freelancer/{id}

	Update freelancer




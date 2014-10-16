KnowYourCongress
====================

An app based on `GovTrack.us <http://govtrack.us/>`_, which allows users to cast votes on bills, and compare their representatives' voting histories to their own.

(Work in progress)



Dependencies
--------------------

All you need to get started is:

- Python 2.7.6
- Virtualenv

(Others will be installed automatically via pip)


Getting Started
---------------------


Django
.......................

::

	cd server
	source bin/env.sh

This will setup a new environment (or find the old one if it's around),
activate the environment, and install requirements to run the django app.
::
	bash bin/run.sh

This will sync the django database, and run the server locally at port 7000, where the javascript looks for the api.

Javascript
.......................

::

	cd client
	bash bin/serve.sh

This will serve the public files with python's SimpleHTTPServer module.
You can then visit the page at localhost:8000.
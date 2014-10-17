KnowYourCongress
====================

An app based on `GovTrack.us <http://govtrack.us/>`_, which allows users to cast votes on bills, and compare their representatives' voting histories to their own.

(Work in progress)



Dependencies
--------------------

All you need to get started is:

- Python 2.7.6
- Virtualenv

Other dependencies can be found in requirements.txt, and are installed via pip.


Getting Started
---------------------

Setup the virtual environment
................................
::

	source bin/env.sh

This will setup a new environment (or find the old one if it's around),
activate the environment, and install requirements to run the django app, and to compile SCSS files.


Server
.......................
::

	bash bin/run_server.sh


This will sync the django database, and run the server locally at port 7000, where the marionette application looks for the api.



Client
.......................
::

	bash bin/serve_client.sh

This will serve the public files with python's SimpleHTTPServer module.
You can then visit the page at `localhost:8000 <http://localhost:8000/>`_.

::

	bash bin/sass_watcher.sh

This will start a watchdog process that monitors SASS/SCSS files for changes,
and recompiles them when updated.


Don't waste time
................................
::

	bash bin/all.sh

This starts up both servers and the watchdog process in a single shell session. The virtual environment must still be activated before running this script.
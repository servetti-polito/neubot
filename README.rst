Neubot DASH
===========

Testing HTTP streaming network neutrality
-----------------------------------------

This is a fork of the neubot project that adds a new test for the DASH
protocol. The test has to be performed against the server hosted on
streaming.polito.it.

At this moment, only the development branch is up to date, no release has been
made. You can clone the development version with this command:

    git clone -b develop https://github.com/servetti-polito/neubot-dash.git

Then, move to the neubot-dash folder:

    cd neubot-dash

To allow the collection of the test results you must have granted us the right
to do that. A quick and dirty trick is to create a database with this
information already set:

    cp scripts/database.sqlite3 .

The DASH test can be run from the command line:

    python ./bin/neubot dash -fv -A streaming.polito.it


Sample output
-------------

Sample output of the dash test:


    WARNING: database: opening database in readonly mode
    dash: run the test in the local process context...
    dash with http://streaming.polito.it:8080/
    dash: negotiate in progress...
    dash: negotiate ... authorized to take the test
    dash: latency in progress...
    dash: latency ...  done, 69.7 ms
    dash: download in progress...
    dash: download - speed: 1894.02638783 (kb/s), elapsed: 0.264585971832 (s), next_rate: 1500 (kb/s), size: 384000 B
    dash: download - speed: 2854.43182963 (kb/s), elapsed: 1.05139684677 (s), next_rate: 2500 (kb/s), size: 640000 B
    dash: download - speed: 2461.11869317 (kb/s), elapsed: 2.03205990791 (s), next_rate: 2000 (kb/s), size: 512000 B
    dash: download - speed: 1971.5443174 (kb/s), elapsed: 2.02944493294 (s), next_rate: 1500 (kb/s), size: 384000 B
    dash: download - speed: 1026.68274273 (kb/s), elapsed: 2.92314314842 (s), next_rate: 900 (kb/s), size: 230400 B
    dash: download - speed: 142074.761959, elapsed: 1.62270903587
    dash: download ...  done, 1.1 Mbit/s
    dash: upload in progress...
    dash: upload - speed: 61942.4605697, elapsed: 1.03625202179
    dash: upload ...  done, 495.5 Kbit/s
    dash: collect in progress...
    WARNING: dash: readonly database
    dash: collect ... done


Check also the Neubot site: http://www.neubot.org/


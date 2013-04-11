neubot
^^^^^^

The network neutrality bot
''''''''''''''''''''''''''

..
.. Copyright (c) 2010-2013
..     Nexa Center for Internet & Society, Politecnico di Torino (DAUIN)
..     and Simone Basso <bassosimone@gmail.com>
..
.. This file is part of Neubot <http://www.neubot.org/>.
..
.. Neubot is free software: you can redistribute it and/or modify
.. it under the terms of the GNU General Public License as published by
.. the Free Software Foundation, either version 3 of the License, or
.. (at your option) any later version.
..
.. Neubot is distributed in the hope that it will be useful,
.. but WITHOUT ANY WARRANTY; without even the implied warranty of
.. MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.. GNU General Public License for more details.
..
.. You should have received a copy of the GNU General Public License
.. along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
..

:Manual section: 1
:Date: @DATE@
:Manual group: Neubot manual
:Version: Neubot 0.4.16.0

SYNOPSIS
````````

|   **neubot** **--help**
|   **neubot** **-V**
|   **neubot** *subcommand* ...

DESCRIPTION
```````````

Neubot is a free-software Internet bot that gathers network performance
data useful to investigate network neutrality. Neubot runs in the
background and periodically performs active network tests with test
servers provided by `Measurement Lab`_ (a distributed server platform
that hosts open network measurement tools). Implemented tests are
described in the `IMPLEMENTED TESTS`_ section.

.. _`Measurement Lab`: http://measurementlab.net/

Neubot does not perform any network test until you grant it the
permission to collect and publish your IP address for research
purposes. Neubot behaves like this because it is developed in the
European Union, thus it must comply with European privacy laws
(which consider IP addresses personal data). More on privacy
aspects in the PRIVACY_ section.

Neubot is a background process. You can control it by using its
subcommands, its web interface or its web API (see, respectively,
the SUBCOMMANDS_, `WEB INTERFACE`_ and `WEB API`_ sections). Neubot
listens for web requests at ``http://127.0.0.1:9774/``. To access
the web interface, use either your favorite browser or the ``viewer``
subcommand. To change the address and/or port where Neubot listens
for web requests, edit ``/etc/neubot/api``.

On UNIX, Neubot runs with the privileges of the ``_neubot`` user
or with the ones of the user indicated in the ``/etc/neubot/users``
configuration file.  On Windows, Neubot is run in the context of
the user session and has user privileges.

The command line interface allows you to get the usage string
(``neubot --help``), get the version number (``neubot -V``), and run a
Neubot's subcommand (``neubot subcommand...``).

SUBCOMMANDS
```````````

This section documents Neubot's subcommands.

neubot bittorrent [-6fv] [-A address] [-p port]
  Asks Neubot to run a *bittorrent* test using the web API and fails
  if Neubot is not running in the background.

  Accepts the following options:

    -6
      Prefer IPv6 to IPv4.

    -A address
      Address of the remote test server.

    -f
      Force the test. Run the test in the local process context
      (instead of using the web API) and override privacy
      settings if needed. Useful for developers and for debugging.

    -p
      Port of the remote test server.

    -v
      Makes the command more verbose.

neubot database [-f database] [action]
  Performs the specified *action*, or prints the database's path
  if no action is specified.  We do not recommended to use this
  command to modify the database while Neubot is running, since
  Neubot's code is not ready for that. *On UNIX systems*, this
  command requires root privileges to modify the database: if you
  are not root, the database is opened in readonly mode.

  Accepts the following options:

    -f database
      Force file. Forces the command to use *database* instead of the default
      database path.

  Implements the following actions:

    delete_all
      Deletes all the results in the database.

    dump
      Dumps to the standard ouput the content of the database in JSON format.

    prune
      Removes results older than one year.

    regen_uuid
      Generates a new random unique identifier (or UUID) for Neubot.

    show
      Pretty prints to the standard ouput the content of the database
      in JSON format.

neubot privacy [-Pt] [-D setting=value] [-f database]
  Manage privacy settings. When invoked without
  options, this command prints the privacy settings value.

  Accepts the following options:

    -D setting=value
      Set privacy setting value. When value is *0* the privacy setting
      is "off", otherwise it is "on".

      Note: this command just modifies the database: you have to
      restart Neubot to make changes effective. To modify privacy
      settings when Neubot is running, we recommend to use the
      web interface.

      Privacy settings:

        informed
          The user has read the privacy policy.

        can_collect
          The user provides the permission to collect his/her IP
          address for research purposes.

        can_publish
          The user provides the permission to publish his/her IP
          address allowing anyone to reuse it for research purposes.

      Note: Neubot performs network tests only when all privacy
      settings are "on".

    -f database
      Force file. Forces the command to use database instead of the
      default database path.

    -P
      Prints privacy policy on the standard output.

    -t
      Test.  Exits with success (exit value *0*) if privacy
      settings are all nonzero.  Exits with failure (exit value
      *nonzero*) if at least one setting is zero.

neubot raw [-6fv] [-A address] [-p port]
  Asks Neubot to run a *raw* test using the web API and fails if
  Neubot is not running in the background.

  Accepts the following options:

    -6
      Prefer IPv6 to IPv4.

    -A address
      Address of the remote test server.

    -f
      Force the test. Run the test in the local process context
      (instead of using the web API) and override privacy
      settings if needed. Useful for developers and for debugging.

    -p
      Port of the remote test server.

    -v
      Makes the command more verbose.

neubot speedtest [-6fv] [-A address] [-p port]
  Asks Neubot to run a *speedtest* test using the web API and fails
  if Neubot is not running in the background.

  Accepts the following options:

    -6
      Prefer IPv6 to IPv4.

    -A address
      Address of the remote test server.

    -f
      Force the test. Run the test in the local process context
      (instead of using the web API) and override privacy
      settings if needed. Useful for developers and for debugging.

    -p
      Port of the remote test server.

    -v
      Makes the command more verbose.

neubot start
  *On MacOS* this command runs launchctl(1), which in turn starts
  Neubot. You must be root to run this command.  On MacOS, Neubot's
  installer configures the system to launch Neubot at startup; i.e.,
  you do not typically need to run this command.

  On MacOS, the start command accepts the following options:

    -d
      Debug. When this flag is specified, Neubot runs in
      the foreground.

    -n
      No auto-updates. When this flag is specified, the privileged
      daemon does not check for updates.

    -v
      Verbose. When this flag is specified, the start command
      is verbose (i.e., it prints on the standard error
      the commands it is about to invoke).

      When both -v and -d are specified, Neubot runs in verbose mode
      in the foreground.

  *On Windows*, the start command runs Neubot with the privileges
  of the user that invokes it. On Windows, Neubot is run when a
  user logs in and runs in the context of the user's session.

  On Windows, the start command accepts the following options:

    -k
      Kill. When -k is specified, Neubot kills an already
      running Neubot instance (if any) before starting up.

      This is used by the automatic updates process: once the new
      version of Neubot is downloaded and installed, the old version
      executes it with `start -k`.

  *On other UNIX systems*, the start command forks the Neubot daemon,
  which drops root privileges and runs in the background.  On such
  systems, this command does not accept any command line option.

neubot status
  This command asks the status of Neubot using the web API.  It
  returns 0 if connect() succeeds and the response is OK, nonzero
  otherwise.

  *On Windows and MacOS* this command accepts the *-v* option,
  which makes it more verbose. *On other UNIX systems*, it does
  not accept any command line option.

neubot stop
  *On MacOS*, this command runs launchctl(1), which in turn stops
  Neubot. You must be root to run this command. On MacOS, this
  command accepts the *-v* option, which makes it more verbose.

  *On Windows and other UNIX systems*, this command uses the web
  API to request Neubot to exit.

neubot viewer [-A address] [-p port]
  Application that shows the web interface by embedding a web
  rendering engine into a window manager's window.

  By default, this command uses 127.0.0.1 as the address and 9774
  as the port. Override the default with by editing the `/etc/neubot/api`
  configuration file. Override the configuration file by using the
  command line, as follows:

    -A address
      Override address where Neubot is listening.

    -p port
      Override port where Neubot is listening.

FILES
`````

Assuming that Neubot is installed at **/usr/local**, this is the
list of the files installed.

/etc/neubot/api
  Configuration file that indicates the endpoint where Neubot should
  listen for web API requests. Example (which also indicates the
  default values)::

    address 127.0.0.1  # Address where the listen
    port 9774          # Port where to listen
 

/etc/neubot/users
  Configuration file that indicates the unprivileged user names
  that Neubot should use. Example (which also indicates the default
  values)::

    update_user _neubot_update  # For auto-updates (MacOS-only)
    unpriv_user _neubot         # For network tests

/usr/local/bin/neubot
  The neubot executable script.

/usr/local/share/neubot/*
  Location where neubot Python modules are installed.

/usr/local/share/neubot/www/*
  Location where the web user interface files are installed.

/user/local/share/neubot/www/test/foo.html
  Description of the *foo* test. It is included into the results.html
  page when the test is selected.

/user/local/share/neubot/www/test/foo.json
  Description of the plots and tables included into results.html
  when test *foo* is selected. The *recipe* that specifies how to
  compute the values to plot and/or write into the tables is written
  in a domain-specific language based on LISP. We describe this
  language below, in the `RECIPE DSL`_ section.

/user/local/share/neubot/www/test/foo.json.local
  User-modified *foo.json* file. When *foo.json.local* is present on
  the filesystem, Neubot uses the user-modified version instead
  of the the stock version. Allows you to heavily customize the
  results page of the *foo* experiment.

/var/lib/neubot/database.sqlite3
  System-wide results database for Linux systems, created when the
  neubot daemon starts for the first time.

/var/neubot/database.sqlite3
  System-wide results database for UNIX systems (except Linux),
  created when the neubot daemon starts for the first time.

EXAMPLES
````````

In this section we represent the unprivileged user prompt with *$*
and the root user prompt with *#*.

Run ondemand `bittorrent` test:

|
|    $ neubot bittorrent

Run ondemand `raw` test:

|
|    $ neubot raw

Run ondemand `speedtest` test:

|
|    $ neubot speedtest

Start **neubot**:

|
|    # neubot start

Stop **neubot**

|
|    # neubot stop  # MacOS
|    $ neubot stop  # other UNIX

Run neubot in foreground with verbose logging "on":

|
|    # neubot start -dv                       # MacOS
|    $ neubot agent -v -D agent.daemonize=no  # other UNIX

Export system-wide results to JSON:

|
|    # neubot database dump > output.json

Run Neubot *command* from the sources directory:

|
|    $ ./bin/neubot *command*

IMPLEMENTED TESTS
`````````````````

TBD

WEB USER INTERFACE
``````````````````

TBD

WEB API
```````

TDB

RECIPE DSL
``````````

TBD

PRIVACY
```````

.. :Version: 2.0.3

The Neubot project is a research effort that aims to study the quality
and neutrality of ordinary users' Internet connections, to rebalance the
information asymmetry between them and Service Providers.  The Neubot
software (i) *measures* the quality and neutrality of your Internet
connection.  The raw measurement results are (ii) *collected* on the
measurement servers for research purposes and (iii) *published*, to allow
other individuals and institutions to reuse them for research purposes.

To *measure* the quality and neutrality of your Internet connection,
the Neubot software does not monitor or analyze your Internet traffic.
It just uses a fraction of your connection capacity to perform background
transmission tests, sending and/or receiving random data.  The results
contain the measured performance metrics, such as the download speed,
or the latency, as well as your computer load, as a percentage, and
*your Internet address*.

The Internet address is paramount because it allows to *infer your Internet
Service Provider* and to have a rough idea of *your location*, allowing to
put the results in context.  The Neubot project needs to *collect* it
to study the data and wants to *publish* it to enable other individuals
and institutions to carry alternative studies and/or peer-review its
measurements and data analysis methodology.  This is coherent with the
policy of the distributed server platform that empowers the Neubot
project, Measurement Lab (M-Lab), which requires all results to be
released as open data [1]_.

You are reading this privacy policy because Neubot is developed in the
European Union, where there is consensus that Internet addresses are
*personal data*.  This means that the Neubot project cannot store, process
or publish your address without your prior *informed consent*, under the
provisions of the "Codice in materia di protezione dei dati personali"
(Decree 196/03) [2]_.  In accordance with the law, data controller is the
NEXA Center for Internet & Society [3]_, represented by its co-director Juan
Carlos De Martin.

Via its web interface [4]_, the Neubot software asks you (a) to explicitly
assert that you are *informed*, i.e. that you have read the privacy
policy, (b) to give it the permission to *collect* and (c) *publish* your
IP address.  If you do not assert (a) and you don't give the permission
to do (b) and (c), Neubot cannot run tests because, if it did, it would
violate privacy laws and/or Measurement Lab policy.

The data controller guarantees you the rights as per Art. 7 of the
above-mentioned Decree 196/03.  Basically, you have total control over
you personal data, and you can, for example, inquire Neubot to remove
your Internet address from its data sets.  To exercise your rights, please
write to <privacy@neubot.org> or to "NEXA Center for Internet & Society,
Dipartimento di Automatica e Infomatica, Politecnico di Torino, Corso Duca
degli Abruzzi 24, 10129 Turin, ITALY."

.. [1] http://www.measurementlab.net/about
.. [2] http://www.garanteprivacy.it/garante/doc.jsp?ID=1311248
.. [3] http://nexa.polito.it/
.. [4] http://127.0.0.1:9774/privacy.html

AUTHOR
``````

Neubot authors are:

|
| Simone Basso                  <bassosimone@gmail.com>
| Antonio Servetti              <antonio.servetti@polito.it>

The following people have contributed patches to the project:

|
| Alessio Palmero Aprosio	<alessio@apnetwork.it>
| Roberto D'Auria		<everlastingfire@autistici.org>
| Marco Scopesi			<marco.scopesi@gmail.com>

The following people have helped with internationalization:

|
| Claudio Artusio               <claudioartusio@gmail.com>

COPYRIGHT
`````````

| Copyright (c) 2010-2013 Nexa Center for Internet & Society,
|     Politecnico di Torino (DAUIN)

| Neubot is free software: you can redistribute it and/or
| modify it under the terms of the GNU General Public License
| as published by the Free Software Foundation, either version
| 3 of the License, or (at your option) any later version.

SEE ALSO
````````

| ``http://www.neubot.org/``
| ``http://github.com/neubot/neubot``
| ``http://twitter.com/neubot``

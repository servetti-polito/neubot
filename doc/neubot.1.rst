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
:Date: 2013-04-11
:Manual group: Neubot manual
:Version: Neubot 0.4.16.0

SYNOPSIS
````````

|   **neubot** **--help**
|   **neubot** **-V**
|   **neubot** *subcommand* ...

DESCRIPTION
```````````

`Neubot`_ is a free-software Internet bot that gathers network performance
data useful to investigate network neutrality. Neubot runs in the
background and periodically performs active network tests with test
servers provided by `Measurement Lab`_ (a distributed server platform
that hosts open network measurement tools). Implemented tests are
described in the `IMPLEMENTED TESTS`_ section.

.. _`Neubot`: http://neubot.org/
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
for web requests, edit ``/etc/neubot/api`` (see the `FILES`_
section).

Neubot runs with the privileges of the ``_neubot`` user,
or with the ones of the user indicated in the ``/etc/neubot/users``
configuration file (see the `FILES`_ section).

The command line interface allows you to get the usage string
(``neubot --help``), get the version number (``neubot -V``) and
run a Neubot's subcommand (``neubot subcommand...``).

IMPLEMENTED TESTS
`````````````````

All Neubot tests receive and send random data. Also, note that Neubot does
not monitor the user's traffic.

Neubot implements three active network tests: ``bittorrent``, ``raw`` and
``speedtest``. For each test, there is a Neubot subcommand that allows
to run the test immediately. Also, note that Neubot schedules one of the
three tests at random every 23 - 27 minutes.

The ``bittorrent`` test emulates BitTorrent peer-wire protocol and
estimates the round-trip time, the download and the upload goodput.
It uses the time that connect() takes to complete as an estimator of
the round-trip time. It estimates the goodput by dividing the amount of
transferred bytes by the elapsed time. To avoid consuming too much
user resources, the ``bittorrent`` test adapts the number of bytes to
transfer such that the test runs for about five seconds.

The ``raw`` test performs a `raw` 10-second TCP download to estimate
the download goodput. Also, it estimates the goodput from the
round-trip time, and it collects statistics about the TCP sender
by using Web100 (see ``http://www.web100.org``). In addition, it
estimates the round-trip time in two ways: (1) by measuring the
time that connect() takes to complete (like ``bittorrent``) and (2)
by measuring the average time elapsed between sending a small request
and receiving a small response.

The ``speedtest`` test emulates HTTP and estimates the round-trip
time, the download and the upload goodput. It estimates the round-trip
time in two ways: (1) by measuring the time that connect() takes
to complete (like ``bittorrent``) and (2) by measuring the average
time elapsed between sending a small request and receiving a small
response (like ``raw``). It estimates the goodput by dividing the
amount of transferred bytes by the elapsed time. To avoid consuming
too much user resources, the ``bittorrent`` test adapts the number
of bytes to transfer such that the test runs for about five seconds.

See the `WEB API`_ section for a description of the results saved
by all the experiments (see, in particular, the ``/api/data``
description).

SUBCOMMANDS
```````````

This section documents Neubot's subcommands.

**neubot bittorrent [-6fv] [-A address] [-p port]**
  Asks Neubot to run a bittorrent test using the web API and fails
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

    -p port
      Port of the remote test server.

    -v
      Makes the command more verbose.

**neubot database [-f database] [action]**
  Performs the specified ``action`` or prints the database's path
  if no action is specified.  We do not recommended to use this
  command to modify the database while Neubot is running, since
  Neubot's does not expect the database to change while it is
  running, so it won't pick the changes up. This command requires
  ``root`` privileges to modify the database: if you are not
  ``root``, the database is opened in readonly mode.

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
      Generates a new random unique identifier (or UUID) for Neubot. (See
      the `PRIVACY`_ section for more on the UUID).

    show
      Pretty prints to the standard ouput the content of the database
      in JSON format.

**neubot privacy [-Pt] [-D setting=value] [-f database]**
  Manage privacy settings. When invoked without
  options, this command prints the current privacy
  settings values.

  Accepts the following options:

    -D setting=value
      Turn on (nonzero) and off (zero) the specified privacy
      setting.

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
      settings are on.

    -f database
      Force file. Forces the command to use database instead of the
      default database path.

    -P
      Prints privacy policy on the standard output.

    -t
      Test.  Exits with success (exit value *0*) if all privacy
      settings all nonzero.  Exits with failure (exit value
      *nonzero*) if at least one setting is zero.

**neubot raw [-6fv] [-A address] [-p port]**
  Asks Neubot to run a raw test using the web API and fails if
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

    -p port
      Port of the remote test server.

    -v
      Makes the command more verbose.

**neubot speedtest [-6fv] [-A address] [-p port]**
  Asks Neubot to run a speedtest test using the web API and fails
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

    -p port
      Port of the remote test server.

    -v
      Makes the command more verbose.

**neubot start**
  On MacOS this command runs launchctl(1), which in turn starts
  Neubot. You must be ``root`` to run this command.  On MacOS, Neubot's
  installer configures the system to launch Neubot at startup; i.e.,
  you do not typically need to run this command.

  (On MacOS, Neubot is implemented by two daemons: the usual unprivileged
  daemon and a privileged daemon. The latter controls the former and
  periodically forks an unprivileged child to check for updates.)

  On MacOS, the start command accepts the following options:

    -a
      Auto-updates. When this flag is specified, the privileged
      daemon periodically forks an unprivileged child to check
      for updates.

    -d
      Debug. When this flag is specified, Neubot runs in
      the foreground.

    -v
      Verbose. When this flag is specified, the start command
      is verbose (i.e., it prints on the standard error
      the commands it is about to invoke).

      When both -v and -d are specified, Neubot runs in verbose mode
      in the foreground.

  At boot time, launchctl(1) starts Neubot with the -a and -d
  command line options.

  On other UNIX systems, the start command forks the Neubot daemon,
  which drops ``root`` privileges and runs in the background.  On such
  systems, this command does not accept any command line option.

**neubot status**
  This command asks the status of Neubot using the web API.  It
  returns 0 if connect() succeeds and the response is OK, nonzero
  otherwise.

  On MacOS this command accepts the ``-v`` option, which makes it
  more verbose. On other UNIX systems, it does not accept any
  command line option.

**neubot stop**
  On MacOS, this command runs launchctl(1), which in turn stops
  Neubot. You must be ``root`` to run this command. On MacOS, this
  command accepts the ``-v`` option, which makes it more verbose.

  On other UNIX systems, this command uses the web
  API to request Neubot to exit.

**neubot viewer**
  This command shows the web interface by embedding a web
  rendering engine into a window manager's window. Currently,
  the only implemented ``viewer`` is based on ``python-webkit``
  and ``pygtk``.

FILES
`````

Assuming that Neubot is installed at ``/usr/local``, this is the
list of the files installed.

**/etc/neubot/api**
  Configuration file that indicates the endpoint where Neubot should
  listen for web API requests. Example (which also shows the syntax
  and indicates the default values)::

    #
    # /etc/neubot/api - controls address, port where Neubot listens
    # for incoming web API requests.
    #
    address 127.0.0.1  # Address where the listen
    port 9774          # Port where to listen
 

**/etc/neubot/users**
  Configuration file that indicates the unprivileged user names
  that Neubot should use. Example (which also shows the syntax
  and indicates the default values)::

    #
    # /etc/neubot/users - controls the unprivileged user names used
    # by Neubot to perform various tasks.
    #
    update_user _neubot_update  # For auto-updates (MacOS-only)
    unpriv_user _neubot         # For network tests

**/usr/local/bin/neubot**
  The Neubot executable script.

**/usr/local/share/neubot/**
  Location where Neubot Python modules are installed.

**/usr/local/share/neubot/www/**
  Location where the web interface files are installed. The web interface
  is described in the `WEB INTERFACE`_ section.

**/var/lib/neubot/database.sqlite3**
  System-wide results database for Linux systems, created when
  Neubot starts for the first time.

**/var/neubot/database.sqlite3**
  System-wide results database for non-Linux systems,
  created when Neubot starts for the first time.

EXAMPLES
````````

In this section we represent the unprivileged user prompt with ``$``
and the ``root`` user prompt with ``#``.

Run on-demand bittorrent test::

    $ neubot bittorrent

Run on-demand raw test::

    $ neubot raw

Run on-demand speedtest test::

    $ neubot speedtest

Start Neubot::

    # neubot start

Stop Neubot::

    # neubot stop  # MacOS
    $ neubot stop  # other UNIX

Run Neubot in the foreground with verbose logging::

    # neubot start -dv                       # MacOS
    $ neubot agent -v -D agent.daemonize=no  # other UNIX

Export Neubot results to JSON::

    # neubot database dump > output.json

Run Neubot ``command`` from the sources directory::

    $ ./bin/neubot command

WEB INTERFACE
`````````````

Neubot web interface uses server side includes (on the server side)
and javascript (and the client side).  On the Javascript side, Neubot
uses jQuery and jqPlot.

Here we provide a brief description of the core files of the web
interface:

**css/**
  Directory that contains CSS files.

**favicon.ico**
  Neubot's favicon.

**footer.html**
  Common footer for all web pages.

**header.html**
  Common header for all web pages.

**img/**
  Directory that contains images.

**js/**
  Directory that contains javascript files. In addition to jQuery and
  jqPlot, it contains the following scripts:

  **js/contrib.js**
    Helper functions from many authors.

  **js/i18n.js**
    Implementation of web user interface internationalization (aka i18n).

  **js/index.js**
    Contains functions to retrieve and process the state of Neubot.

  **js/log.js**
    Contains code to retrieve and process Neubot logs.

  **js/privacy.js**
    Contains code to query and modify privacy settings.

  **js/results.js**
    Contains code to process Neubot results, as well as code to display
    them as plots and tables. 

  **js/settings.js**
    Contains code to retrieve and modify Neubot settings.

  **js/state.js**
    Helper code for retrieving and processing Neubot state.

  **js/update.js**
    Minimal script included by updater.html. It just sets the active
    tab in the web interface.

  **js/utils.js**
    Miscellaneous helper functions.

**lang/**
  Directory that contains one javascript file for each translation of
  the web interface. Each of these javascripts contains a dictionary, named
  ``LANG``, that maps a string (or a key representing a string) to its
  translation.

  In javascript, you mark strings for translation by wrapping them
  with ``i18n.get()`` calls. For example, to indicate that the string
  "Disable automatic tests" should be translated, you should write::

    ...
    i18n.get("Disable automatic tests");

  In HTML code, you mark the content of an HTML tag for translation by adding
  the tag to the ``i18n`` class. Differently from javascript, we don't map
  the content of an HTML tag to its translation; instead, we map a key that
  represents the HTML tag content to its translation. The key is another HTML
  class, which must start with ``i18n_``, as in the following example::

    ...
    <p class="i18n i18n_foobar">Neubot web interface</p>

  To translate the two examples above in, for example, Italian you
  edit the ``www/lang/it.css`` file and add::

    var LANG = {
        ...
        "Disable automatic tests": "Disabilita test automatici",
        "i18n_foobar": "Interfaccia web di Neubot",
        ...
    };

**log.html**
  Shows Neubot logs.

**not_running.html**
  Page displayed when Neubot is not running.

**privacy.html**
  Shows (and allows to modify) privacy settings.

**results.html**
  The results page, dynamically filled by javascript using Neubot web
  API. It allows you to see the results of recent experiments, both
  in form of plots and tables. 

**settings.html**
  Shows (and allows to modify) Neubot settings.

**test/**
  Directory that contains a ``foo.html`` and a ``foo.json`` file for
  each test ``foo``. The list of available tests in ``results.html`` is
  automatically generated from the files in this directory.

  **test/foo.html**
    Description of the ``foo`` test. It is included into the
    ``results.html`` page when the test is selected.

  **test/foo.json**
    Description of the plots and tables included into ``results.html``
    when test ``foo`` is selected. The format of the JSON is documented
    into the `WEB API`_ section (see ``/api/results`` description).

  **test/foo.json.local**
    When ``foo.json.local`` exists, Neubot will use it (instead of
    ``foo.json``) to prepare plots and tables in ``results.html``.
    Allows the user to heavily customize the results page for test
    ``foo``.

**update.html**
  Page displayed on Windows when Neubot needs to be manually
  updated. Now that automatic updates are implemented, it
  should never pop up.

WEB API
```````

To access Neubot API, send HTTP requests to the address and port
where Neubot is listening (which is 127.0.0.1:9774 by default, and
which can be changed by editing ``/etc/neubot/api``).

Here is a detailed description of each API.

**/api**
  This API is an alias for ``/api/``.

**/api/**
  This API responds to ``GET``, ``POST`` with a JSON encoding a list
  of strings. Each string is the path of one available API.

  Example output::

    [
     "/api",
     "/api/",
     "/api/results",
     "/api/config",
     "/api/debug",
     "/api/exit",
     "/api/index",
     "/api/log",
     "/api/runner",
     "/api/state",
     "/api/version"
   ]

**/api/config**
  This API allows to get (``GET``) and set (``POST``) the configuration
  variables that modify the behavior of Neubot.

  The configuration object is a dictionary. ``GET`` returns a dictionary,
  encoded using JSON, that contains the whole configuration object. ``POST``
  sends an url-encoded string, which typically contains the variables you
  want to change only.

  The API accepts the following query-string options:

  **debug=integer**
    When nonzero, the API returns a pretty-printed JSON. Otherwise, the
    JSON is serialized on a single line.

  **labels=integer**
    When nonzero, returns the description of the variables instead of their
    values.

  Example::

    {
     "enabled": 1,
     "negotiate.max_thresh": 64,
     "negotiate.min_thresh": 32,
     "negotiate.parallelism": 7,
     "privacy.can_collect": 1,
     "privacy.can_publish": 1,
     "privacy.can_informed": 1,
     ...
     "uuid": "0964312e-f451-4579-9984-3954dcfdeb42",
     "version": "4.2",
     "www.lang": "default"
    }

  We have not standardized variable names yet. Therefore, we don't provide
  here a list of variable names, types and default values.

**/api/debug**
  This API allows you to ``GET`` information about Neubot internals, which
  is typically useful for debugging purposes. As such, the consistency
  of the output format is not guaranteed.

  Example::

    {'WWW': '/usr/share/neubot/www',
     'notifier': {'_subscribers': {},
               '_timestamps': {'statechange': 1336727245277393,
                               'testdone': 1336727245277246}},
     'queue_history': [],
     'typestats': {'ABCMeta': 26,
                   'BackendNeubot': 1,
                   'BackendProxy': 1,
                   ...
                  }}

**/api/data?test=string**
  This API allows you to retrieve the data collected during Neubot tests
  via the ``GET`` method. As we have a single API for all tests, you
  must provide the test name using the query string.

  This API returns a JSON that serializes a list of dictionaries, in which
  each dictionary is the data collected during a test.

  The API accepts the following query-string parameters:

  **test=string**
    This parameter is mandatory and specifies the test whose data you
    want to retrieve.

  **since=integer**
    Returns only the data collected after the specified time (indicated
    as the number of seconds elapsed since the midnight of January, 1st 1970).

  **until=integer**
    Returns only the data collected before the specified time (indicated
    as the number of seconds elapsed since midnight of January, 1st 1970).

  **debug=integer**
    When nonzero, the API returns a pretty-printed JSON. Otherwise, the
    JSON is serialized on a single line.

  We represent the data collected by the ``bittorrent`` test with a
  dictionary that contains the following fields:

    **connect_time (float)**
      RTT estimated by measuring the time that connect() takes
      to complete, measured in seconds.

    **download_speed (float)**
      Download speed measured by dividing the number of received bytes over
      the elapsed download time, measured in bytes over seconds.

    **internal_address (string)**
      Neubot's IP address, as seen by Neubot. It is typically either
      an IPv4 or an IPv6 address.

    **neubot_version (string)**
      Neubot version number, encoded as a floating point number and
      printed into a string. Given a version number in the format
      ``<major>.<minor>.<patch>.<revision>``, the encoding is as follows::

        <major> + 1e-03 * <minor> + 1e-06 * <patch>
                + 1e-09 * <revision>

      For example, the ``0.4.15.3`` version number
      is encoded as ``0.004015003``.

    **platform (string)**
      The operating system platform, e.g. ``linux2``, ``win32``.

    **privacy_can_collect (integer)**
      The value of the ``can_collect`` privacy setting.

    **privacy_can_publish (integer)**
      The value of the ``can_publish`` privacy setting.

    **privacy_informed (integer)**
      The value of the ``informed`` privacy setting.

    **real_address (string)**
      Neubot's IP address, as seen by the server. It is typically either
      an IPv4 or an IPv6 address.

    **remote_address (string)**
      The server's IP address. It is typically either an IPv4 or an
      IPv6 address.

    **timestamp (integer)**
      Time when the test was performed, expressed as number of seconds
      elapsed since midnight of January, 1st 1970.

    **upload_speed (float)**
      Upload speed measured by dividing the number of sent bytes over the
      elapsed upload time, measured in bytes over seconds.

    **uuid (string)**
      Random unique identifier of the Neubot instance, useful to perform
      time series analysis.

  Example::

   [
    {
     "connect_time": 0.003387928009033203, 
     "download_speed": 4242563.145733707, 
     "internal_address": "130.192.91.231", 
     "neubot_version": "0.004015007", 
     "platform": "linux2", 
     "privacy_can_collect": 1, 
     "privacy_can_publish": 1, 
     "privacy_informed": 1, 
     "real_address": "130.192.91.231", 
     "remote_address": "194.116.85.224", 
     "test_version": 1, 
     "timestamp": 1366045628, 
     "upload_speed": 4231443.875881268, 
     "uuid": "7528d674-25f0-4ac4-aff6-46f446034d81"
    }, 
    ...

  We represent the data collected by the ``raw`` test with a
  dictionary that contains the following fields:

    **connect_time (float)**
      RTT estimated by measuring the time that connect() takes
      to complete, measured in seconds.

    **download_speed (float)**
      Download speed measured by dividing the number of received bytes over
      the elapsed download time, measured in bytes over seconds.

    **json_data (string)**
      This string contains the serialization of a JSON object, which
      contains all the data collected during the test.

      Note: on the server side, the ``raw`` test only saves the data
      contained inside ``json_data``. On client side, we wrap such
      data with a dictionary that has the same field names of the
      ``bittorrent`` and ``speedtest`` test, because that simplifies
      its processing in ``js/results.js``.

      The data encoded into this field is the data that is actually saved
      on server side. Historically, we wrapped this data into a dictionary
      that has fields with names similar to the ``bittorrent`` and
      ``speedtest`` ones, because ``js/results.js`` expected fields with
      fixed names.

    **internal_address (string)**
      Neubot's IP address, as seen by Neubot. It is typically either
      an IPv4 or an IPv6 address.

    **latency (float)**
      RTT estimated by measuring the average time elapsed between sending
      a small request and receiving a small response, measured in seconds.

    **neubot_version (float)**
      Neubot version number, encoded as a floating point number and printed
      into a string. Given a version number in the format
      ``<major>.<minor>.<patch>.<revision>``, the encoding is as follows::

        <major> + 1e-03 * <minor> + 1e-06 * <patch>
                + 1e-09 * <revision>

      For example, the ``0.4.15.3`` version number
      is encoded as ``0.004015003``.

    **platform (string)**
      The operating system platform, e.g. ``linux2``, ``win32``.

    **real_address (string)**
      Neubot's IP address, as seen by the server. It is typically either
      an IPv4 or an IPv6 address.

    **remote_address (string)**
      The server's IP address. It is typically either an IPv4 or an
      IPv6 address.

    **timestamp (integer)**
      Time when the test was performed, expressed as number of seconds
      elapsed since midnight of January, 1st 1970.

    **uuid (string)**
      Random unique identifier of the Neubot instance, useful to perform
      time series analysis.

  Example::

   [
    {
     "connect_time": 0.2981860637664795, 
     "download_speed": 3607.120929707688, 
     "internal_address": "130.192.91.231", 
     "json_data": "...", 
     "latency": 0.29875500202178956, 
     "neubot_version": "0.004015007", 
     "platform": "linux2", 
     "real_address": "130.192.91.231", 
     "remote_address": "203.178.130.237", 
     "timestamp": 1365071100, 
     "uuid": "7528d674-25f0-4ac4-aff6-46f446034d81"
    },
    ...

  Once unserialized, the JSON object saved into the ``json_data`` field
  of the ``raw`` dictionary (henceforth, 'outer dictionary') is a
  dictionary that contains the following fields:

    **al_capacity (float)**
      Median bottleneck capacity computed at application level. We are
      still doing research to assess the reliability of this field.

    **al_mss (float)**
      MSS according to the application level (information gathered
      using setsockopt(2)).

    **al_rexmits (list)**
      Likely retransmission events computed at application level. We are
      still doing research to assess the reliability of this field.

    **alrtt_list (list of floats)**
      List of RTT samples estimated by measuring the average time elapsed
      between sending a small request and receiving a small response,
      measured in seconds.

    **alrtt_avg (float)**
      Same as ``latency`` in the outer dictionary.

    **connect_time (float)**
      Same as ``connect_time`` in the outer dictionary.

    **goodput (float)**
      Same as ``download_speed`` in the outer dictionary.

    **goodput_snap (list of dictionaries)**
      List that contains a dictionary, which is updated roughly every
      second during the download, and which contains the following fields:

      **ticks (float)**
        Time when the current dictionary was saved, expressed as number
        of seconds since midnight of January, 1st 1970.

      **bytesdiff (integer)**
        Number of bytes received since stats were previously saved.

      **timediff (float)**
        Number of seconds elapsed since stats were previously saved.

      **utimediff (float)**
        Difference between current ``tms_utime`` field of the ``tms``
        struct modified by ``times(3)`` and the previous value of
        the same field.

      **stimediff (float)**
        Difference between current ``tms_stime`` field of the ``tms``
        struct modified by ``times(3)`` and the previous value of
        the same field.

    **myname (string)**
      Neubot's address (according to the server). This is same as
      ``real_address`` in the outer dictionary.

    **peername (string)**
      Servers's address. This is same as ``server_address`` in the outer
      dictionary.

    **platform (string)**
      Same as ``platform`` in the outer dictionary.

    **uuid (string)**
      Same as ``uuid`` in the outer dictionary.

    **version (string)**
      Same as ``neubot_version`` in the outer dictionary.

  Example::

   [
    {
     "client": {
      "al_mss": 1448, 
      "uuid": "7528d674-25f0-4ac4-aff6-46f446034d81", 
      "goodput": {
       "bytesdiff": 128200, 
       "timediff": 35.540810108184814, 
       "ticks": 1365071098.203412
      }, 
      "al_rexmits": [], 
      "connect_time": 0.2981860637664795, 
      "alrtt_list": [
       0.31011295318603516, 
       0.30966901779174805, 
       0.29677391052246094, 
       0.2957899570465088, 
       0.29570794105529785, 
       0.2956199645996094, 
       0.29558706283569336, 
       0.2956211566925049, 
       0.2958400249481201, 
       0.296828031539917
      ], 
      "myname": "130.192.91.231", 
      "peername": "203.178.130.237", 
      "platform": "linux2", 
      "version": "0.004015007", 
      "al_capacity": 10982553.692585895, 
      "alrtt_avg": 0.29875500202178956, 
      "goodput_snap": [
       {
        "bytesdiff": 24616, 
        "timediff": 1.0001380443572998, 
        "ticks": 1365071063.66274, 
        "stimediff": 0.0, 
        "utimediff": 0.0
       }, 
       ...
      ]
     }, 
     "server": {
      "timestamp": 1365070933, 
      "myname": "203.178.130.237", 
      "peername": "130.192.91.231", 
      "platform": "linux2", 
      "version": "0.004015007", 
      "goodput": {
       "bytesdiff": 131092, 
       "timediff": 34.94503116607666, 
       "ticks": 1365070933.95337
      }, 
      "goodput_snap": [
       {
        "bytesdiff": 31856, 
        "timediff": 1.0005459785461426, 
        "ticks": 1365070900.008885, 
        "stimediff": 0.0, 
        "utimediff": 0.0
       }, 
       ...
      ], 
      "web100_snap": []
     }
    }

  We represent the data collected by the ``speedtest`` test with a
  dictionary that contains the following fields:

    **connect_time (float)**
      RTT estimated by measuring the time that connect() takes
      to complete, measured in seconds.

    **download_speed (float)**
      Download speed measured by dividing the number of received bytes over
      the elapsed download time, measured in bytes over seconds.

    **internal_address (string)**
      Neubot's IP address, as seen by Neubot. It is typically either
      an IPv4 or an IPv6 address.

    **latency (float)**
      RTT estimated by measuring the average time elapsed between sending
      a small request and receiving a small response, measured in seconds.

    **neubot_version (string)**
      Neubot version number, encoded as a floating point number and printed
      into a string. Given a version number in the format
      ``<major>.<minor>.<patch>.<revision>``, the encoding is as follows::

        <major> + 1e-03 * <minor> + 1e-06 * <patch>
                + 1e-09 * <revision>

      For example, the ``0.4.15.3`` version number
      is encoded as ``0.004015003``.

    **platform (string)**
      The operating system platform, e.g. ``linux2``, ``win32``.

    **privacy_can_collect (integer)**
      The value of the ``can_collect`` privacy setting.

    **privacy_can_publish (integer)**
      The value of the ``can_publish`` privacy setting.

    **privacy_informed (integer)**
      The value of the ``informed`` privacy setting.

    **real_address (string)**
      Neubot's IP address, as seen by the server. It is typically either
      an IPv4 or an IPv6 address.

    **remote_address (string)**
      The server's IP address. It is typically either an IPv4 or an
      IPv6 address.

    **timestamp (integer)**
      Time when the test was performed, expressed as number of seconds
      elapsed since midnight of January, 1st 1970.

    **upload_speed (float)**
      Upload speed measured by dividing the number of sent bytes over the
      elapsed upload time, measured in bytes over seconds.

    **uuid (string)**
      Random unique identifier of the Neubot instance, useful to perform
      time series analysis.

  Example::

   [
    {
     "connect_time": 0.0017991065979003906, 
     "download_speed": 11626941.501993284, 
     "internal_address": "130.192.91.231", 
     "latency": 0.003973397341641513, 
     "neubot_version": "0.004015007", 
     "platform": "linux2", 
     "privacy_can_collect": 1, 
     "privacy_can_publish": 1, 
     "privacy_informed": 1, 
     "real_address": "130.192.91.231", 
     "remote_address": "194.116.85.237", 
     "test_version": 1, 
     "timestamp": 1365074302, 
     "upload_speed": 10974865.674026133, 
     "uuid": "7528d674-25f0-4ac4-aff6-46f446034d81"
    }, 
    ...

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

Neubot authors are::

  Simone Basso                  <bassosimone@gmail.com>
  Antonio Servetti              <antonio.servetti@polito.it>

The following people have contributed patches to the project::

  Alessio Palmero Aprosio	<alessio@apnetwork.it>
  Roberto D'Auria		<everlastingfire@autistici.org>
  Marco Scopesi			<marco.scopesi@gmail.com>

The following people have helped with internationalization::

  Claudio Artusio               <claudioartusio@gmail.com>

COPYRIGHT
`````````

Neubot as a collection is::

  Copyright (c) 2010-2013 Nexa Center for Internet & Society,
      Politecnico di Torino (DAUIN)
 
  Neubot is free software: you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation, either version
  3 of the License, or (at your option) any later version.

SEE ALSO
````````

- http://www.neubot.org/
- http://github.com/neubot/neubot
- http://twitter.com/neubot

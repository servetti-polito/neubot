# neubot/notifier_core.py

#
# Copyright (c) 2012-2013
#     Nexa Center for Internet & Society, Politecnico di Torino (DAUIN)
#     Simone Basso <bassosimone@gmail.com>
#
# Copyright (c) 2011
#     Marco Scopesi <marco.scopesi@gmail.com>
#
# This file is part of Neubot <http://www.neubot.org/>.
#
# Neubot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Neubot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
#

""" Core notification mechanism """

#
# This is the most annoying notification strategy ever, as pointed out
# by Gianni Bosio (my reference usability guru) some time ago.  However,
# this is also the simplest and works.  To have a good Win32 and MacOS
# notification mechanism is not a priority yet, so feel free to contribute
# something if you are annoyed by browser notifications.  I am looking to
# Python-based solutions that rely on PyObjC on MacOS and on PyWin32 on
# Windows.
#

import getopt
import logging
import sys
import time

if __name__ == "__main__":
    sys.path.insert(0, ".")

from neubot.config import CONFIG

from neubot import browser
from neubot import utils
from neubot import utils_net

class NotifierCore(object):
    """ Core notification mechanism """

    def __init__(self):
        """ Initialize browser notifications """
        self.last_show = {}

    def loop(self):
        """ Main loop """
        while True:
            address, port = background_api.get_address_port()
            if " " in address:
                for address in address.split():
                    if self.contact_neubot(address, port):
                        break
            else:
                self.contact_neubot(address, port)

    def contact_neubot(self):
        """ Contact Neubot, retrive information and perform actions """
        try:
            return self._contact_neubot()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            logging.warning("notifier_core: unhandled exception", exc_info=1)
            return False

    def _contact_neubot(self):
        """ Contact Neubot, retrive information and perform actions """
        connection = lib_http.HTTPConnection(address, port)

        connection.request("GET", "/api/config")
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError("Invalid response code: %d" % response.status)
        body = response.read()
        connection.close()
        config = json.loads(body)

        connection.request("GET", "/api/state")
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError("Invalid response code: %d" % response.status)
        body = response.read()
        connection.close()
        state = json.loads(body)

        if privacy.count_valid(config, "privacy.") != 3:
            self.notify_bad_privacy(config)

        if "update" in state:
            self.notify_update_avail(state)

        return True

    def notify_bad_privacy(self, dct):
        """ Notify that privacy settings are invalid """
        logging.warning("notifier_core: invalid privacy settings: %s", dct)

    def notify_update_avail(self, dct):
        """ Notify that an update is available """
        logging.warning("notifier_core: update available: %s", dct)


    def notify_page(self, html_page):
        """ Open a webpage to notify the user """

        #
        # If Neubot is disabled and the user does not want to
        # receive notifications when it is disabled, then make
        # sure we don"t annoy her.
        # Do not prompt the user too frequently, because it may
        # become TOO ANNOYING if the browser opens every fifteen
        # minutes or so.  Reported some time ago by a user who
        # complained with me at the phone.
        #

        logging.debug("notifier_browser: maybe notify: %s", html_page)

        honor_enabled = CONFIG["notifier_browser.honor_enabled"]
        enabled = CONFIG["enabled"]
        if not enabled and honor_enabled:
            logging.debug("notifier_browser: honoring enabled")
            return

        now = utils.timestamp()
        last_show = self.last_show.get(html_page, 0)
        min_interval = CONFIG["notifier_browser.min_interval"]
        if now - last_show < min_interval:
            logging.debug("notifier_browser: avoid spamming the user")
            return

        self.last_show[html_page] = now

        address, port = background_api.get_address_port()
        uri = "http://%s/%s" % (
                                   utils_net.format_epnt((address, port)),
                                   html_page
                                )

        return browser.open_browser(uri)

    def notify_bad_privacy(self):
        """ Tell the user that privacy settings are bad """
        self.notify_page("privacy.html")

    def notify_update_avail(self):
        """ Tell the user that a new version is available """
        self.notify_page("update.html")

NOTIFIER_BROWSER = NotifierBrowser()

def main(args):
    """ Main function """

    try:
        options, arguments = getopt.getopt(args[1:], "D:t:v")
    except getopt.error:
        sys.exit("usage: notifier_browser [-v] [-D setting] [-t time] page...")
    if not arguments:
        sys.exit("usage: notifier_browser [-v] [-D setting] [-t time] page...")

    sleeptime = 0
    for name, value in options:
        if name == "-D":
            CONFIG.register_property(value)
        elif name == "-t":
            sleeptime = int(value)
        elif name == "-v":
            CONFIG["verbose"] = 1

    CONFIG.merge_properties()

    for argument in arguments:
        if argument == "privacy":
            NOTIFIER_BROWSER.notify_bad_privacy()
        elif argument == "update":
            NOTIFIER_BROWSER.notify_update_avail()
        else:
            sys.exit("Invalid page.  Valid pages are: privacy, update")

        if sleeptime:
            logging.debug("notifier_browser: sleep for %d seconds", sleeptime)
            time.sleep(sleeptime)

if __name__ == "__main__":
    main(sys.argv)

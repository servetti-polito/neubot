# neubot/notifier_core.py

#
# Copyright (c) 2012-2013
#     Nexa Center for Internet & Society, Politecnico di Torino (DAUIN)
#     and Simone Basso <bassosimone@gmail.com>
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

import errno
import getopt
import logging
import socket
import sys
import time

if __name__ == "__main__":
    sys.path.insert(0, ".")

from neubot.compat import json
from neubot.six.moves import http_client

from neubot import background_conf
from neubot import privacy

class NotifierCore(object):
    """ Core notification mechanism """

    def __init__(self, interval):
        """ Initialize browser notifications """
        self.interval = interval

    def loop(self):
        """ Main loop """
        while True:
            address, port = background_conf.get_address_port()
            if " " in address:
                for address in address.split():
                    if self.contact_neubot(address, port):
                        break
            else:
                self.contact_neubot(address, port)
            logging.debug("notifier_core: sleep for %d s...", self.interval)
            time.sleep(self.interval)
            logging.debug("notifier_core: sleep for %d s... done",
                          self.interval)

    def contact_neubot(self, address, port):
        """ Contact Neubot, retrive information and perform actions """
        try:
            return self._contact_neubot(address, port)
        except (KeyboardInterrupt, SystemExit):
            raise
        except socket.error:
            error = sys.exc_info()[1]
            if error.args[0] == errno.ECONNREFUSED:
                logging.warning("notifier_core: connection refused")
            else:
                logging.warning("notifier_core: unhandled exception",
                                exc_info=1)
            return False
        except:
            logging.warning("notifier_core: unhandled exception", exc_info=1)
            return False

    def _contact_neubot(self, address, port):
        """ Contact Neubot, retrive information and perform actions """

        logging.debug("notifier_core: connect to %s:%s...", address, port)
        connection = http_client.HTTPConnection(address, port)
        connection.connect()
        logging.debug("notifier_core: connect to %s:%s... done", address, port)

        logging.debug("notifier_core: GET /api/config...")
        connection.request("GET", "/api/config")
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError("Invalid response code: %d" % response.status)
        body = response.read()
        connection.close()
        config = json.loads(body)
        logging.debug("notifier_core: GET /api/config... %s", config)

        logging.debug("notifier_core: GET /api/state...")
        connection.request("GET", "/api/state")
        response = connection.getresponse()
        if response.status != 200:
            raise RuntimeError("Invalid response code: %d" % response.status)
        body = response.read()
        connection.close()
        state = json.loads(body)
        logging.debug("notifier_core: GET /api/state... %s", state)

        logging.debug("notifier_core: process config and state...")
        if privacy.count_valid(config, "privacy.") != 3:
            self.notify_bad_privacy(config)
        if "update" in state:
            self.notify_update_avail(state)
        logging.debug("notifier_core: process config and state... done")

        return True

    def notify_bad_privacy(self, dct):
        """ Notify that privacy settings are invalid """

    def notify_update_avail(self, dct):
        """ Notify that an update is available """

class NotifierLogger(NotifierCore):
    """ Notifies events using the logger """

    def notify_bad_privacy(self, dct):
        logging.warning("notifier_core: invalid privacy settings: %s", dct)

    def notify_update_avail(self, dct):
        logging.warning("notifier_core: update available: %s", dct)

if __name__ == "__main__":

    def main(args):
        """ Main function """

        try:
            options, arguments = getopt.getopt(args[1:], "vt:")
        except getopt.error:
            sys.exit("usage: notifier_core [-v] [-t interval]")
        if arguments:
            sys.exit("usage: notifier_core [-v] [-t interval]")

        interval = 30
        for name, value in options:
            if name == "-t":
                interval = int(value)
            elif name == "-v":
                logging.getLogger().setLevel(logging.DEBUG)

        NotifierLogger(interval).loop()

    main(sys.argv)

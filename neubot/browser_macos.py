# neubot/browser_macos.py

#
# Copyright (c) 2012 Simone Basso <bassosimone@gmail.com>,
#  NEXA Center for Internet & Society at Politecnico di Torino
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

''' MacOS open browser driver '''

import subprocess
import sys

def open_browser(uri):
    ''' Open browser on Windows NT '''

    #
    # Use the best tool available on the platform to load Neubot
    # web user interface in the default browser.
    # FIXME As suggested by Vittorio Bertola and Simone Caldana this
    # app does not behave as the user expects because it just opens the
    # browser and then exits.  (Please, note that open -W would not
    # help to fix this issue because the icon will keep jumping in the
    # dashboard and that is even more confusing.)  I think the right
    # fix here is to create a Cocoa application that uses the WebView
    # class to load the proper page.
    #

    verbose = 0
    cmdline = ['/usr/bin/open', uri]
    if verbose:
        sys.stderr.write('DEBUG: about to exec: %s\n' % str(cmdline))
    retval = subprocess.call(cmdline)
    if verbose:
        sys.stderr.write('DEBUG: return value: %d\n' % retval)

    return retval == 0

def main(args):
    ''' Main function '''
    open_browser(args[1])

if __name__ == '__main__':
    main(sys.argv)
